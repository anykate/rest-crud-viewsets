from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'crudviewsets'


router = routers.DefaultRouter()
router.register('', views.EmployeeViewset)


urlpatterns = [
    path('', views.saveemployee, name='save_employee_data'),
    path('api/employees/', include(router.urls)),
]
