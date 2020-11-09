import os
import json
import django
import logging
import requests
from json import JSONDecodeError

from django.db import transaction
from django.utils import timezone

from apscheduler.schedulers.blocking import BlockingScheduler

from app.enums import HTTPMethod
from app.models import RestRequest, RestResponse

os.environ["DJANGO_SETTINGS_MODULE"] = "scheduler.settings"
django.setup()

scheduler = BlockingScheduler()

HTTP_METHODS = {
    HTTPMethod.GET: requests.get,
    HTTPMethod.POST: requests.post,
    HTTPMethod.PATCH: requests.patch,
    HTTPMethod.DELETE: requests.delete,
}

logger = logging.getLogger(__name__)


@scheduler.scheduled_job('interval', seconds=1)
def execute_scheduled_requests():
    logger.info('Started to execute scheduled requests.')
    with transaction.atomic():
        rest_requests = RestRequest.objects.select_for_update().filter(started__lte=timezone.now(), completed=None)
        for rest_request in rest_requests:
            logger.info(rest_request)
            headers = None
            payload = None
            status_code = 400
            func = HTTP_METHODS.get(rest_request.method)
            try:
                response = func(rest_request.url, rest_request.payload)
            except Exception as exc:
                logger.error(exc)
            else:
                headers = dict(response.headers)
                status_code = response.status_code
                try:
                    payload = json.loads(response.text)
                except JSONDecodeError:
                    payload = response.text
            rest_response = RestResponse.objects.get_or_create(
                headers=headers,
                status_code=status_code,
                data=payload,
                rest_request_id=rest_request.id,
            )
            logger.info(rest_response)
            rest_request.completed = timezone.now()
            rest_request.save()
    logger.info('Ended process.')


scheduler.start()
