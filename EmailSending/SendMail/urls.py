from django.urls import path
from .views import sendmail

urlpatterns=[
    path('mail/',sendmail,name='mail'),

]