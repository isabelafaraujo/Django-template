from rest_framework import serializers
from registration import models


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Registration
        fields = '_all_'
