from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='Полное имя')
    job_title = models.CharField(max_length=150, verbose_name='Посада')
    profile_url = models.CharField(max_length=250, verbose_name='Профиль')
    location = models.CharField(max_length=250, verbose_name='Локация')
    email = models.EmailField(max_length=254, verbose_name='Эл. адрес')
    phone_number = models.CharField(max_length=254, verbose_name='Номер телефона')

    def __str__(self):
        return self.full_name


class Company(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    company_url = models.CharField(max_length=250, verbose_name='Компания')
    location = models.CharField(max_length=150, verbose_name='Локация')
    income = models.CharField(max_length=150, verbose_name='Доход')

