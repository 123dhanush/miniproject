from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("validate/",views.validate,name='validate'),
    path("validate/add/",views.add,name="add"),
    path("validate/dele/",views.dele,name="dele"),
    path("validate/cal/",views.cal,name="cal"),
    path("validate/sche/",views.sche,name="sche"),
    path("validate/que/",views.que,name="que"),
    path("validate/dates/",views.dates,name="dates"),
    path("validate/dates_confidential/",views.datesconfidential,name="dates_confidential"),
    path("validate/update/",views.update,name="update"),
]
