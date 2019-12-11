from .models import Expedientes
import django_filters


class ExpedientesFilter(django_filters.FilterSet):
    observacion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Expedientes
        fields = ['observacion', 'user_carga']
