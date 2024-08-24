import django_filters
from django.core.exceptions import FieldDoesNotExist
from django.db.models import Q

from log_module.models import Log


class LogFilter(django_filters.FilterSet):
    time = django_filters.DateTimeFilter(field_name='time', lookup_expr='exact')
    time__gte = django_filters.DateTimeFilter(field_name='time', lookup_expr='gte')
    time__lte = django_filters.DateTimeFilter(field_name='time', lookup_expr='lte')
    remote_ip = django_filters.CharFilter(field_name='remote_ip', lookup_expr='exact')
    remote_user = django_filters.CharFilter(field_name='remote_user', lookup_expr='icontains')
    request_method = django_filters.CharFilter(field_name='request_method', lookup_expr='icontains')
    request_path = django_filters.CharFilter(field_name='request_path', lookup_expr='icontains')
    request_protocol = django_filters.CharFilter(field_name='request_protocol', lookup_expr='icontains')
    response_code = django_filters.NumberFilter(field_name='response_code', lookup_expr='exact')
    response_size = django_filters.NumberFilter(field_name='response_size', lookup_expr='gte')
    referrer = django_filters.CharFilter(field_name='referrer', lookup_expr='icontains')
    agent = django_filters.CharFilter(field_name='agent', lookup_expr='icontains')
    search = django_filters.CharFilter(method='filter_by_all_fields')

    class Meta:
        model = Log
        fields = [
            'time', 'remote_ip', 'remote_user', 'request_method',
            'request_path', 'request_protocol', 'response_code',
            'response_size', 'referrer', 'agent'
        ]

    # Compile a query that includes search by all fields of a model
    def filter_by_all_fields(self, queryset, name, value):
        if not value:
            return queryset
        query = Q()
        for field_name in self.Meta.fields:
            try:
                field = self.Meta.model._meta.get_field(field_name)
                query |= Q(**{f'{field.name}__icontains': value})
            except FieldDoesNotExist:
                continue
        return queryset.filter(query)
