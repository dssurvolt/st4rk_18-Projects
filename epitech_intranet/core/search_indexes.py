from haystack import indexes
from .models import Message

class MessageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    sender = indexes.CharField(model_attr='sender__username')
    recipient = indexes.CharField(model_attr='recipient__username')
    content = indexes.CharField(model_attr='content')
    sent_at = indexes.DateTimeField(model_attr='sent_at')

    def get_model(self):
        return Message

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
