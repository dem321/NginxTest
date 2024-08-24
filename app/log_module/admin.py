from django.contrib import admin

from log_module.models import Log


# Register your models here.
class LogAdmin(admin.ModelAdmin):
    list_display = (
        'time', 'remote_ip', 'remote_user', 'request_method', 'request_path', 'request_protocol', 'response_code',
        'response_size', 'referrer', 'agent')
    list_filter = (
        'time', 'remote_user', 'request_method', 'request_path', 'request_protocol', 'response_code', 'referrer',
        'agent')
    search_fields = (
        'time', 'remote_ip', 'remote_user', 'request_method', 'request_path', 'request_protocol', 'response_code',
        'response_size', 'referrer', 'agent')


admin.site.register(Log, LogAdmin)
