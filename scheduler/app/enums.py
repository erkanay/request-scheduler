from django.db import models


class HTTPMethod(models.TextChoices):
    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    UPDATE = "UPDATE"
    PATCH = "PATCH"
    DELETE = "DELETE"
