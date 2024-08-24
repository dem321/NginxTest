from rest_framework import pagination
from rest_framework.response import Response


# Custom paginator to return customized response
class CustomLogPaginator(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100
    queryset = None
    project = None

    def get_page_size(self, request):
        if self.page_size_query_param in request.query_params:
            return int(request.query_params[self.page_size_query_param])
        return self.page_size

    def get_paginated_response(self, data):
        page_size = self.get_page_size(self.request)
        total_pages = (self.page.paginator.count + page_size - 1) // page_size if page_size else 0
        return Response({'total_pages': total_pages, 'page_size': page_size, 'obj_count': self.page.paginator.count,
                         'data': data, 'additional_data': 'additional data example'})
