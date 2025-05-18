from rest_framework import serializers
from .models import Fonctionnaire, BulletinPaie

class FonctionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fonctionnaire
        fields = '__all__'

class BulletinPaieSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletinPaie
        fields = '__all__'