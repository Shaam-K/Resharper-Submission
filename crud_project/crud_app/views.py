from django.shortcuts import render
from crud_app.forms import create_form
from crud_app.models import table_contents

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def forms_edit(request):
    form = create_form()
    if form.is_valid():
        form.save()
        
    context = {'form': form}
    return render(request, "index.html", context)