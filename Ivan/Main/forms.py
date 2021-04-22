from django import forms
from .models import Client, CarBrand, ClientCar, CarBodyType, Work
from datetime import date, datetime


class ClientForm(forms.ModelForm):
    registration_date = forms.DateField(
        required=False,
        label="Registration_date",
    )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("registration_date") is None:
            cleaned_data["registration_date"] = date.today()
        return cleaned_data

    class Meta:
        model = Client
        fields = "__all__"


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = "__all__"


class ClientCarForm(forms.ModelForm):
    class Meta:
        model = ClientCar
        fields = "__all__"


class CarBodyTypeForm(forms.ModelForm):
    class Meta:
        model = CarBodyType
        fields = "__all__"


class WorkForm(forms.ModelForm):
    start_work = forms.DateTimeField(
        required=False,
        label="Start work"
    )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("start_work") is None:
            cleaned_data["start_work"] = datetime.now()
        return cleaned_data

    class Meta:
        model = Work
        fields = "__all__"
