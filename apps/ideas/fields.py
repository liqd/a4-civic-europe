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
    re_decimal is a regex that is sliced from the entered values, the original
    regex (zeros after a decimal point) is overwritten here, in order to raise
    a validation error for decimal values with only zeros after decimal
    """
    re_decimal = re.compile(r'')
