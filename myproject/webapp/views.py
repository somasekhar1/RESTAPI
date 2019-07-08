from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serialize import Employeeserialization
class EmployeeList(APIView):
        def get(self,request):
            emp=Employee.objects.all()
            serializer=Employeeserialization(emp,many=True)
            return Response(serializer.data)
        def pest(self):
            pass