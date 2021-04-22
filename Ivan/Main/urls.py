from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.home, name="home"),
    url(r"^DB_(?P<table_name>[\w]+)", views.db_form)
]
