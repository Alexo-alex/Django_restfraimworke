from rest_framework import serializers
from .models import *


class PersonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('full_name', 'profile_url')


class PersonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        exclude = ()


class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'company_url')


class CompanyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        exclude = ()
