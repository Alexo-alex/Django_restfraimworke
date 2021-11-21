from urllib import request

from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializer import *
from .models import *


def get_persons(request):
    persons = Person.objects.all()
    return render(request, '', persons)


class PersonListView(APIView):

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonListSerializer(persons, many=True)
        return Response(serializer.data)



class PersonDetailView(APIView):

    def get(self, request, pk):
        person = Person.objects.get(id=pk)
        serializer = PersonDetailSerializer(person)
        return Response(serializer.data)


class CompanyListView(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanyListSerializer(company, many=True)
        return Response(serializer.data)


class CompanyDetailView(APIView):

    def get(self, request, pk):
        company = Company.objects.get(id=pk)
        serializer = CompanyDetailSerializer(company)
        return Response(serializer.data)
