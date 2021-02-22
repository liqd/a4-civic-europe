import re

from django.db import models
from django.forms import fields


class CustomIntegerField(models.IntegerField):

    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': CustomIntegerFormField,
            **kwargs,
        })


class CustomIntegerFormField(fields.IntegerField):
    """
    overwrites re_decimal = re.compile(r'\.0*\s*$'), in order to raise
    a validation error for decimal values with only 0s after decimal
    """
    re_decimal = re.compile(r'')
