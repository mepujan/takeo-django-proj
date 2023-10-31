from django.urls import path
from .views import format_date_time,acccess_quote
urlpatterns = [
     path("",format_date_time, name="index"),
     path("quote",acccess_quote,name="access-quote")
]
