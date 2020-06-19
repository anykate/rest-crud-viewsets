import requests

from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Employee
from .forms import EmployeeInsertForm
from .serializers import EmployeeSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = 'employee_id'


def saveemployee(request):
    form = EmployeeInsertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            post_data = requests.post(
                'http://localhost:8000/api/employees/',
                headers={'Content-Type': 'application/json'},
                json=form.cleaned_data
            )
            return redirect('/')
    return render(request, 'core/insert.html', {'form': form})
