from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size = 100
    page_size_query_param = 'page_size'
