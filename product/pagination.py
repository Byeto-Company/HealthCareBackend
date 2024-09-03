from rest_framework.pagination import LimitOffsetPagination


class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10