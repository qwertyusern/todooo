from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *
s=serializers.ModelSerializer
class RejaSer(s):
    class Meta:
        model=Reja
        fields="__all__"