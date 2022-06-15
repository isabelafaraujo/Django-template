from rest_framework import viewsets
from api.registration.apiModules import serializers
from api.registration import models


class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegistrationSerializer
    queryset = models.Registration.objects.all()
