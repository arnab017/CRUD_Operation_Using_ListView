from django.shortcuts import render
from django.views.generic import ListView
from app.models import *
# Create your views here.

class SchoolList(ListView):
    model = School
    context_object_name = 'all_SO'
    