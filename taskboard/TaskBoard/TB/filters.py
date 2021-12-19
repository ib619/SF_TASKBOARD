from django_filters import FilterSet
from .models import Response


class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = {
            'article__title': ['icontains'],
        }
