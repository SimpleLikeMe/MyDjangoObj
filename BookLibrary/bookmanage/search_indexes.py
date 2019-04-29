from haystack import indexes
from .models import *


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(doucument=True, use_template=True)

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

