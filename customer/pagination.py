from rest_framework.pagination import LimitOffsetPagination


class CustomerLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10