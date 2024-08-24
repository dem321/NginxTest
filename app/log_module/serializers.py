import datetime

from rest_framework import serializers

from .models import Log


# Custom serializer that aggregates data from nginx log to Log object
class LogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = [
            'time', 'remote_ip', 'remote_user', 'request_method',
            'request_path', 'request_protocol', 'response_code',
            'response_size', 'referrer', 'agent'
        ]

    def to_internal_value(self, data):
        internal_data = data.copy()
        if 'time' in internal_data:
            internal_data['time'] = datetime.datetime.strptime(internal_data['time'], '%d/%b/%Y:%H:%M:%S %z')
        internal_data['response_code'] = internal_data.get('response', None)
        internal_data['response_size'] = internal_data.get('bytes', None)
        request = internal_data.get('request', None)
        if request:
            request_info = request.split(' ')
            if len(request_info) == 3:
                internal_data['request_method'] = request_info[0]
                internal_data['request_path'] = request_info[1]
                internal_data['request_protocol'] = request_info[2]
        return super().to_internal_value(internal_data)


class LogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        exclude = ['id']
