from django.shortcuts import render

from people.models import Person


def list_people(request):
    return render(request, "people/list_people.html", {"people": Person.objects.all()})
