from django.contrib import admin
from .models import RestRequest, RestResponse


class RESTResponseInline(admin.StackedInline):
    model = RestResponse
    list_display = ("headers", "status_code", "data")


class RestRequestAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
    inlines = [RESTResponseInline]


admin.site.register(RestRequest, RestRequestAdmin)
admin.site.register(RestResponse)
