import uuid
from django.db import models # Changed from django.contrib.gis.db
from django.utils.translation import gettext_lazy as _
from identity.models import User

class Property(models.Model):
    """
    Miroir local des actifs fonciers sur la Blockchain.
    Source de vérité = Smart Contract.
    """
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', _('Brouillon / En attente')
        VALIDATING = 'VALIDATING', _('En cours de validation')
        ON_CHAIN = 'ON_CHAIN', _('Sécurisé sur Blockchain')
        DISPUTED = 'DISPUTED', _('En litige')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Blockchain Link
    on_chain_id = models.DecimalField(max_digits=78, decimal_places=0, unique=True, null=True, blank=True, help_text="Token ID (uint256) sur le contrat")
    owner_wallet = models.ForeignKey(User, on_delete=models.PROTECT, related_name='properties', to_field='wallet_address', db_column='owner_wallet')
    
    # Geospatial Data (Fallback JSON for No-GDAL env)
    # TODO: Switch back to PointField/PolygonField in Production with PostGIS
    gps_centroid = models.JSONField(help_text="Point central {lat: float, lng: float}")
    gps_boundaries = models.JSONField(help_text="Limites exactes [ {lat, lng}, ... ]")
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT, db_index=True)
    last_sync_block = models.BigIntegerField(null=True, blank=True, help_text="Dernier bloc synchronisé")

    class Meta:
        db_table = 'properties'
        verbose_name = _("Propriété")
        verbose_name_plural = _("Propriétés")
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['owner_wallet']),
        ]

    def __str__(self):
        return f"Prop {self.id} ({self.status})"

class PropertyMedia(models.Model):
    """
    Liens vers les documents stockés sur IPFS.
    Aucun fichier binaire n'est stocké en base.
    """
    class MediaType(models.TextChoices):
        PHOTO_LAND = 'PHOTO_LAND', _('Photo du Terrain')
        PHOTO_DOC = 'PHOTO_DOC', _('Photo Document Papier')
        VIDEO_DRONE = 'VIDEO_DRONE', _('Vidéo Drone')
        LEGAL_DOC = 'LEGAL_DOC', _('Document Juridique (PDF/Scan)')
        OTHER_MEDIA = 'OTHER_MEDIA', _('Autre Média')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='media')
    
    ipfs_cid = models.CharField(max_length=64, help_text="Content ID IPFS (ex: Qm...)")
    media_type = models.CharField(max_length=20, choices=MediaType.choices)
    is_verified = models.BooleanField(default=False, help_text="Hash confirmé sur la blockchain ?")
    
    class Meta:
        db_table = 'property_media'

    def __str__(self):
        return f"{self.media_type} for {self.property_id}"

class BlockchainSyncStatus(models.Model):
    """
    État de santé de l'Indexeur.
    """
    class SyncStatus(models.TextChoices):
        OK = 'OK', _('Synchronisé')
        LAGGING = 'LAGGING', _('En retard')
        STOPPED = 'STOPPED', _('Arrêté / Erreur')

    contract_address = models.CharField(max_length=42, primary_key=True)
    chain_id = models.IntegerField(default=137, help_text="Chain ID (ex: 137 Polygon)")
    last_processed_block = models.BigIntegerField(default=0)
    sync_status = models.CharField(max_length=20, choices=SyncStatus.choices, default=SyncStatus.OK)

    class Meta:
        db_table = 'blockchain_sync_status'

    def __str__(self):
        return f"Sync {self.contract_address}: {self.last_processed_block}"
