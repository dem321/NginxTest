from django.db import models


class Log(models.Model):
    time = models.DateTimeField('The timestamp when the server received the request')
    remote_ip = models.GenericIPAddressField('The IP address of the client that made the request')
    remote_user = models.CharField('The authenticated user making the request', max_length=100)
    request_method = models.CharField('The HTTP method', max_length=100)
    request_path = models.CharField('The requested path', max_length=100)
    request_protocol = models.CharField('The HTTP protocol with version', max_length=100)
    response_code = models.IntegerField('The HTTP status code returned by the server', )
    response_size = models.IntegerField('The size of the response in bytes', )
    referrer = models.CharField('The Referer header, indicating the URL of '
                                'the page that linked to the requested resource',
                                max_length=100)
    agent = models.CharField('The User-Agent header, describing the client software', max_length=100)
