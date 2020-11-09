from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel

from app.enums import HTTPMethod


class RestRequest(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=6, choices=HTTPMethod.choices)
    url = models.URLField(null=False, blank=False)
    payload = models.JSONField(null=True, blank=True)
    started = models.DateTimeField(null=True, blank=True)
    completed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "rest request"
        verbose_name_plural = "rest requests"
        ordering = ["started"]

    def __str__(self):
        return f'Request (started={self.started}, completed={self.completed})'

    # add a post signal to trigger celery task


class RestResponse(TimeStampedModel):
    rest_request = models.OneToOneField(RestRequest, on_delete=models.CASCADE)
    status_code = models.PositiveSmallIntegerField()
    headers = models.JSONField(null=True)
    data = models.JSONField(null=True)

    class Meta:
        verbose_name = "rest response"
        verbose_name_plural = "rest responses"
        ordering = ["rest_request__started"]

    def __str__(self):
        return f'Response (status_code={self.status_code}, request_id={self.rest_request.id})'
