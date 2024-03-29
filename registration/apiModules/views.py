from rest_framework import viewsets
from registration.apiModules import serializers
from registration import models


class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegistrationSerializer
    queryset = models.Registration.objects.all()
