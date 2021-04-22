from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Client
from .forms import ClientForm, CarBodyTypeForm, CarBrandForm, ClientCarForm, WorkForm


# Create your views here.
def home(request):
    all_clients = Client.objects.all()
    context = {
        "clients": all_clients,
    }
    return render(request, "Home.html", context)


def db_form(request, table_name):
    if table_name == "Client":
        Form = ClientForm
    elif table_name == "CarBodyType":
        Form = CarBodyTypeForm
    elif table_name == "CarBrand":
        Form = CarBrandForm
    elif table_name == "ClientCar":
        Form = ClientCarForm
    elif table_name == "Work":
        Form = WorkForm
    else:
        raise Exception("Incorrect table name")

    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    context = {
        "form": form,
    }
    return render(request, "DB_Form.html", context)
