from django import forms
from .models import Client, CarBrand, ClientCar, CarBodyType, Work
from datetime import date, datetime


class ClientForm(forms.ModelForm):
    """
INSERT INTO Client (
     first_name,
     last_name,
     registration_date,
     contact_number
    ) VALUES (
     get_from_form_first_name,
     get_from_form_last_name,
     get_from_form_registration_date,
     get_from_form_contact_number
    );
    """
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
    """
INSERT INTO CarBrand (
     brand
    ) VALUES (
     get_from_form_brand
    );
    """
    class Meta:
        model = CarBrand
        fields = "__all__"


class ClientCarForm(forms.ModelForm):
    """
INSERT INTO ClientCar (
     client,
     brand,
     body_type
    ) VALUES (
     get_from_form_id_client,
     get_from_form_id_car_brand,
     get_from_form_id_car_body_type
    );
    """
    class Meta:
        model = ClientCar
        fields = "__all__"


class CarBodyTypeForm(forms.ModelForm):
    """
INSERT INTO CarBodyType (
     body_type
    ) VALUES (
     get_from_form_body_type
    );
    """
    class Meta:
        model = CarBodyType
        fields = "__all__"


class WorkForm(forms.ModelForm):
    """
INSERT INTO Work (
     client,
     car,
     start_work,
     end_work
    ) VALUES (
     get_from_form_id_client,
     get_from_form_id_client_car,
     get_from_form_start_work,
     get_from_form_end_work
    );
    """
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
