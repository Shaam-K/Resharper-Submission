from django.shortcuts import render
from crud_app.models import table_contents

# Create your views here.
def homepage(request):
    return render(request, "index.html")


def mysql_data(request):
    objects = table_contents.objects.all()

    context = {'data' : objects}

    return render(request, "index.html", context)