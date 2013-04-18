from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render;
from architect.models import Architect, Project, Classification


def index( request ):
    render = "Welcome to Fintzy Raveh London"
    return HttpResponse( render )


