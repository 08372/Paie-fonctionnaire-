from rest_framework import viewsets
from .models import Fonctionnaire, BulletinPaie
from .serializers import FonctionnaireSerializer, BulletinPaieSerializer

class FonctionnaireViewSet(viewsets.ModelViewSet):
    queryset = Fonctionnaire.objects.all()
    serializer_class = FonctionnaireSerializer

class BulletinPaieViewSet(viewsets.ModelViewSet):
    queryset = BulletinPaie.objects.all()
    serializer_class = BulletinPaieSerializer