from rest_framework.authentication import TokenAuthentication


class SchedulerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
