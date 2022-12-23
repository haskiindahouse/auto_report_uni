from django.db import transaction
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django import forms
from ..models import Teacher


@login_required
def user_data(request):
    user = Teacher.objects.all()
    return render(request, "profile.html", {"user": user})

