from . import views
from django.urls import path

urlpatterns = [

    path("checkfacultylogin",views.checkfacultylogin,name="checkfacultylogin"),
    path("facultyhome",views.facultyhome,name="facultyhome"),
    path("myfcourses",views.facultycourses,name="facultycourses"),
    path('facultychangepwd', views.facultychangepwd, name='facultychangepwd'),
    path('facultyupdatepwd', views.facultyupdatepwd, name='facultyupdatepwd'),


]