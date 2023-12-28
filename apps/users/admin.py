# flake8: noqa E401
from django.contrib import admin
from django.urls import path

from .models import User

admin.site.register(User)  # Assuming User is your model
