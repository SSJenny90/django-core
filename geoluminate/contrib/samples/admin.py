from typing import Any

from django.contrib.gis import admin
from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicChildModelFilter, PolymorphicParentModelAdmin

from geoluminate.utils import get_subclasses

from .models import BaseSample, Date, Description, Location


class DescriptionInline(admin.TabularInline):
    model = Description
    fields = ["type", "text"]
    extra = 0
    max_num = 2


class DateInline(admin.TabularInline):
    model = Date
    extra = 0
    fields = ["type", "date"]


@admin.register(BaseSample)
class SampleParentAdmin(PolymorphicParentModelAdmin):
    base_model = BaseSample
    child_models = get_subclasses(BaseSample, include_self=True)
    list_display = ["id", "name", "created"]
    exclude = ["options"]
    list_filter = (PolymorphicChildModelFilter,)

    def save_form(self, request: Any, form: Any, change: Any) -> Any:
        print(form.data)
        return super().save_form(request, form, change)


@admin.register(Location)
class LocationAdmin(admin.GISModelAdmin):
    list_display = ["name", "latitude", "longitude", "elevation"]


class SampleAdmin(PolymorphicChildModelAdmin):
    base_model = BaseSample
    inlines = [DescriptionInline, DateInline]
