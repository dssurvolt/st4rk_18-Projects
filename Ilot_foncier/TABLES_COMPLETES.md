# iLÔT FONCIER - TABLES COMPLÈTES (Suite)
## Spécifications détaillées des 25 tables

---

## TABLE 4 : VERIFICATIONS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: verifications (CŒUR MÉTIER)                           ║
║  Volume: 500M lignes | Criticité: TRÈS HAUTE                  ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • user_id               UUID              [FK→users]         ║
║  • property_id           UUID              [FK→properties]    ║
║  • country_id            UUID              [FK→countries]     ║
║  • verification_code     VARCHAR(20)       [UNIQUE] NOT NULL  ║
║  • verification_method   ENUM                                 ║
║    └─ [QR_SCAN, PHOTO_OCR, MANUAL_INPUT, API_LOOKUP]          ║
║  • result_status         ENUM              NOT NULL           ║
║    └─ [AUTHENTIC, SUSPICIOUS, FRAUDULENT, NOT_FOUND, ERROR]   ║
║  • confidence_score      INT (0-100)       NOT NULL           ║
║  • processing_time_ms    INT                                  ║
║  • fraud_indicators      JSON                                 ║
║  • api_response          JSON                                 ║
║  • ip_address            INET                                 ║
║  • geolocation           POINT                                ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║  • completed_at          TIMESTAMP                            ║
║                                                               ║
║  PARTITIONING:                                                ║
║  • Par DATE (RANGE) - 1 partition/mois                        ║
║  • Sub-partition par PAYS (LIST)                              ║
║  • Ex: verifications_2026_01_BJ (27M lignes)                  ║
║  • Gain: 50x plus rapide                                      ║
║                                                               ║
║  INDEX: user_id, property_id, country_id, code, status, date  ║
║  CONTRAINTES: CHECK (confidence_score BETWEEN 0 AND 100)      ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLE 5 : VERIFICATION_RESULTS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: verification_results (1:1 avec verifications)         ║
║  Volume: 500M lignes                                          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • verification_id       UUID              [FK→verifications] ║
║    └─ UNIQUE (relation 1:1)                                   ║
║  • title_authentic       BOOLEAN                              ║
║  • owner_verified        BOOLEAN                              ║
║  • no_disputes           BOOLEAN                              ║
║  • taxes_up_to_date      BOOLEAN                              ║
║  • zone_secure           BOOLEAN                              ║
║  • document_quality      INT (0-100)                          ║
║  • red_flags             JSON                                 ║
║    └─ [{flag: "multiple_sales", severity: "high"}]            ║
║  • recommendations       TEXT                                 ║
║  • detailed_analysis     JSON                                 ║
║  • report_pdf_url        VARCHAR(500)                         ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║                                                               ║
║  INDEX: verification_id (UNIQUE)                              ║
║  CONTRAINTES: CHECK (document_quality BETWEEN 0 AND 100)      ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLE 6 : FRAUD_SIGNALS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: fraud_signals (Alertes IA)                            ║
║  Volume: 25M lignes (5% des vérifications)                    ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • verification_id       UUID              [FK→verifications] ║
║  • signal_type           ENUM              NOT NULL           ║
║    └─ [MULTIPLE_SALES, FAKE_DOCUMENT, DISPUTED_PROPERTY,      ║
║         PRICE_ANOMALY, OWNERSHIP_CONFLICT]                    ║
║  • severity              ENUM              NOT NULL           ║
║    └─ [LOW, MEDIUM, HIGH, CRITICAL]                           ║
║  • description           TEXT              NOT NULL           ║
║  • evidence              JSON                                 ║
║  • ai_confidence         DECIMAL(5,2)                         ║
║  • is_false_positive     BOOLEAN           DEFAULT NULL       ║
║  • reviewed_by           UUID              [FK→users]         ║
║  • reviewed_at           TIMESTAMP         NULL               ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║                                                               ║
║  INDEX: verification_id, signal_type, severity, created_at    ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLE 7 : TRANSACTIONS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: transactions (Escrow intégré)                         ║
║  Volume: 10M lignes                                           ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • transaction_number    VARCHAR(30)       [UNIQUE] NOT NULL  ║
║  • property_id           UUID              [FK→properties]    ║
║  • seller_id             UUID              [FK→users]         ║
║  • buyer_id              UUID              [FK→users]         ║
║  • notary_id             UUID              [FK→users] NULL    ║
║  • country_id            UUID              [FK→countries]     ║
║  • amount_local          DECIMAL(15,2)     NOT NULL           ║
║  • amount_usd            DECIMAL(15,2)     NOT NULL           ║
║  • currency_code         VARCHAR(3)        NOT NULL           ║
║  • escrow_status         ENUM              DEFAULT 'PENDING'  ║
║    └─ [PENDING, FUNDED, HELD, RELEASED, CANCELLED, REFUNDED]  ║
║  • payment_method        ENUM              NOT NULL           ║
║    └─ [MOBILE_MONEY, BANK_TRANSFER, CARD, CASH, CRYPTO]       ║
║  • commission_amount     DECIMAL(10,2)     DEFAULT 0          ║
║  • transaction_status    ENUM              DEFAULT 'INITIATED'║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║  • completed_at          TIMESTAMP         NULL               ║
║                                                               ║
║  INDEX: property_id, seller_id, buyer_id, status, created_at  ║
║  CONTRAINTES:                                                 ║
║  • CHECK (amount_local > 0)                                   ║
║  • CHECK (seller_id != buyer_id)                              ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLE 8 : LISTINGS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: listings (Marketplace)                                ║
║  Volume: 5M lignes                                            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • property_id           UUID              [FK→properties]    ║
║  • seller_id             UUID              [FK→users]         ║
║  • listing_type          ENUM              NOT NULL           ║
║    └─ [SALE, RENT, LEASE]                                     ║
║  • price_local           DECIMAL(15,2)     NOT NULL           ║
║  • price_usd             DECIMAL(15,2)     NOT NULL           ║
║  • is_negotiable         BOOLEAN           DEFAULT TRUE       ║
║  • title                 VARCHAR(200)      NOT NULL           ║
║  • description           TEXT              NOT NULL           ║
║  • status                ENUM              DEFAULT 'ACTIVE'   ║
║    └─ [DRAFT, ACTIVE, SOLD, RENTED, EXPIRED, SUSPENDED]       ║
║  • views_count           INT               DEFAULT 0          ║
║  • favorites_count       INT               DEFAULT 0          ║
║  • featured              BOOLEAN           DEFAULT FALSE      ║
║  • published_at          TIMESTAMP                            ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║                                                               ║
║  INDEX: property_id, seller_id, status, price_usd, published  ║
║  PARTIAL INDEX: ON (status) WHERE status = 'ACTIVE'           ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLE 9 : INQUIRIES

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: inquiries (Messages acheteur→vendeur)                 ║
║  Volume: 15M lignes                                           ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • listing_id            UUID              [FK→listings]      ║
║  • sender_id             UUID              [FK→users]         ║
║  • receiver_id           UUID              [FK→users]         ║
║  • subject               VARCHAR(200)                         ║
║  • message               TEXT              NOT NULL           ║
║  • status                ENUM              DEFAULT 'UNREAD'   ║
║    └─ [UNREAD, READ, REPLIED, CLOSED]                         ║
║  • replied_at            TIMESTAMP         NULL               ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║                                                               ║
║  INDEX: listing_id, sender_id, receiver_id, status, created_at║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLE 10 : PROPERTY_DOCUMENTS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: property_documents                                    ║
║  Volume: 200M fichiers                                        ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • property_id           UUID              [FK→properties]    ║
║  • document_type         ENUM              NOT NULL           ║
║    └─ [TITLE_DEED, CADASTRAL_PLAN, TAX_RECEIPT, CONTRACT,     ║
║         ID_CARD, OTHER]                                       ║
║  • file_name             VARCHAR(255)      NOT NULL           ║
║  • file_url              VARCHAR(500)      NOT NULL           ║
║  • file_size_bytes       BIGINT                               ║
║  • mime_type             VARCHAR(100)                         ║
║  • is_verified           BOOLEAN           DEFAULT FALSE      ║
║  • ocr_extracted_text    TEXT                                 ║
║  • uploaded_by           UUID              [FK→users]         ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║                                                               ║
║  INDEX: property_id, document_type, is_verified, created_at   ║
║  ON DELETE: CASCADE (si propriété supprimée)                  ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLE 11 : PROPERTY_PHOTOS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: property_photos                                       ║
║  Volume: 150M images                                          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • property_id           UUID              [FK→properties]    ║
║  • photo_url             VARCHAR(500)      NOT NULL           ║
║  • thumbnail_url         VARCHAR(500)                         ║
║  • caption               VARCHAR(255)                         ║
║  • display_order         INT               DEFAULT 0          ║
║  • is_primary            BOOLEAN           DEFAULT FALSE      ║
║  • uploaded_by           UUID              [FK→users]         ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║                                                               ║
║  INDEX: property_id, is_primary, display_order                ║
║  CONTRAINTES: Un seul is_primary = TRUE par property          ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLE 12 : USER_PROFILES

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: user_profiles (1:1 avec users)                        ║
║  Volume: 100M lignes                                          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • user_id               UUID              [FK→users] UNIQUE  ║
║  • bio                   TEXT                                 ║
║  • date_of_birth         DATE                                 ║
║  • gender                ENUM                                 ║
║    └─ [MALE, FEMALE, OTHER, PREFER_NOT_TO_SAY]                ║
║  • address_line_1        VARCHAR(255)                         ║
║  • address_line_2        VARCHAR(255)                         ║
║  • city_id               UUID              [FK→cities]        ║
║  • notification_settings JSON                                 ║
║  • privacy_settings      JSON                                 ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║  • updated_at            TIMESTAMP         DEFAULT NOW()      ║
║                                                               ║
║  INDEX: user_id (UNIQUE), city_id                             ║
║  ON DELETE: CASCADE (si user supprimé)                        ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLE 13 : USER_VERIFICATIONS (KYC)

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: user_verifications (KYC)                              ║
║  Volume: 20M lignes                                           ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  • id                    UUID              [PK] NOT NULL      ║
║  • user_id               UUID              [FK→users]         ║
║  • verification_level    ENUM              NOT NULL           ║
║    └─ [LEVEL_1, LEVEL_2, LEVEL_3]                             ║
║  • document_type         ENUM              NOT NULL           ║
║    └─ [ID_CARD, PASSPORT, DRIVERS_LICENSE, PROOF_ADDRESS]     ║
║  • document_url          VARCHAR(500)      NOT NULL           ║
║    └─ Chiffré AES-256                                         ║
║  • document_number       VARCHAR(100)                         ║
║  • verification_status   ENUM              DEFAULT 'PENDING'  ║
║    └─ [PENDING, APPROVED, REJECTED]                           ║
║  • verified_by           UUID              [FK→users]         ║
║  • rejection_reason      TEXT                                 ║
║  • expires_at            DATE                                 ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║                                                               ║
║  INDEX: user_id, verification_level, status                   ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLES GÉOGRAPHIQUES (4 tables)

### TABLE 14 : REGIONS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: regions (Départements/États)                          ║
║  Volume: ~500 lignes                                          ║
╠═══════════════════════════════════════════════════════════════╣
║  • id                    UUID              [PK] NOT NULL      ║
║  • country_id            UUID              [FK→countries]     ║
║  • name_local            VARCHAR(100)      NOT NULL           ║
║  • name_en               VARCHAR(100)                         ║
║  • code                  VARCHAR(10)                          ║
║  • center_point          POINT                                ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
╚═══════════════════════════════════════════════════════════════╝
```

### TABLE 15 : CITIES

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: cities (Villes/Communes)                              ║
║  Volume: ~12 000 lignes                                       ║
╠═══════════════════════════════════════════════════════════════╣
║  • id                    UUID              [PK] NOT NULL      ║
║  • region_id             UUID              [FK→regions]       ║
║  • country_id            UUID              [FK→countries]     ║
║  • name_local            VARCHAR(100)      NOT NULL           ║
║  • population            INT                                  ║
║  • avg_price_per_sqm     DECIMAL(10,2)                        ║
║  • center_point          POINT                                ║
╚═══════════════════════════════════════════════════════════════╝
```

### TABLE 16 : DISTRICTS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: districts (Quartiers)                                 ║
║  Volume: ~50 000 lignes                                       ║
╠═══════════════════════════════════════════════════════════════╣
║  • id                    UUID              [PK] NOT NULL      ║
║  • city_id               UUID              [FK→cities]        ║
║  • name_local            VARCHAR(100)      NOT NULL           ║
║  • avg_price_per_sqm     DECIMAL(10,2)                        ║
║  • center_point          POINT                                ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## TABLES AUDIT & SYSTÈME (5 tables)

### TABLE 17 : AUDIT_LOGS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: audit_logs (Traçabilité 7 ans)                        ║
║  Volume: 1B+ lignes                                           ║
╠═══════════════════════════════════════════════════════════════╣
║  • id                    UUID              [PK] NOT NULL      ║
║  • user_id               UUID              [FK→users]         ║
║  • action_type           ENUM              NOT NULL           ║
║    └─ [CREATE, UPDATE, DELETE, LOGIN, LOGOUT]                 ║
║  • table_name            VARCHAR(50)                          ║
║  • record_id             UUID                                 ║
║  • old_values            JSON                                 ║
║  • new_values            JSON                                 ║
║  • ip_address            INET                                 ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
║                                                               ║
║  PARTITIONING: Par DATE (1 partition par trimestre)           ║
║  ARCHIVAGE: > 2 ans vers tape backup                          ║
╚═══════════════════════════════════════════════════════════════╝
```

### TABLE 18 : USER_SESSIONS

```
╔═══════════════════════════════════════════════════════════════╗
║  TABLE: user_sessions (Sessions actives)                      ║
║  Volume: 5M lignes (purge auto > 30 jours)                    ║
╠═══════════════════════════════════════════════════════════════╣
║  • id                    UUID              [PK] NOT NULL      ║
║  • user_id               UUID              [FK→users]         ║
║  • session_token         VARCHAR(500)      [UNIQUE] NOT NULL  ║
║  • device_info           JSON                                 ║
║  • ip_address            INET                                 ║
║  • last_activity_at      TIMESTAMP         DEFAULT NOW()      ║
║  • expires_at            TIMESTAMP         NOT NULL           ║
║  • created_at            TIMESTAMP         DEFAULT NOW()      ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## RÉCAPITULATIF DES 25 TABLES

| # | Table | Volume | Criticité | Partitionnement |
|---|-------|--------|-----------|-----------------|
| 1 | countries | 54 | Haute | Non |
| 2 | users | 100M | Haute | Non |
| 3 | properties | 50M | Haute | Non |
| 4 | verifications | 500M | **Très Haute** | **Oui (mois+pays)** |
| 5 | verification_results | 500M | Haute | Non |
| 6 | fraud_signals | 25M | Moyenne | Non |
| 7 | transactions | 10M | Haute | Non |
| 8 | listings | 5M | Moyenne | Non |
| 9 | inquiries | 15M | Basse | Non |
| 10 | property_documents | 200M | Moyenne | Non |
| 11 | property_photos | 150M | Basse | Non |
| 12 | user_profiles | 100M | Moyenne | Non |
| 13 | user_verifications | 20M | Haute | Non |
| 14 | regions | 500 | Basse | Non |
| 15 | cities | 12K | Basse | Non |
| 16 | districts | 50K | Basse | Non |
| 17 | audit_logs | 1B+ | **Très Haute** | **Oui (trimestre)** |
| 18 | user_sessions | 5M | Basse | Non |
| 19-25 | Tables auxiliaires | Variable | Variable | Selon besoin |

---

**Stockage Total:** 507 TB  
**Tables partitionnées:** 2 (verifications, audit_logs)  
**Tables avec index spatial:** 4 (properties, regions, cities, districts)  
**Tables chiffrées:** 3 (users.password, user_verifications.document_url, transactions.payment_ref)
