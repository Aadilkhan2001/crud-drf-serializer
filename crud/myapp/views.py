from django.http import JsonResponse
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializers
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# simple rendering a one web page to handle apis 
def indexview(request):
    return render(request,'index.html')


# api logic for retriving all data and adding data into modal using serializer
@csrf_exempt
def AddRetriveEmployee(request):
    employee = Employee.objects.all()
    if request.method == 'GET':
        employee_serialized = EmployeeSerializers(employee,many=True) #serialiing python query object
        return JsonResponse(data=employee_serialized.data,safe=False) # sending response to client in json format
    elif request.method == 'POST':
        request_data=request.body 
        stream = io.BytesIO(request_data)  
        form_data=JSONParser().parse(stream)
        serialized_data=EmployeeSerializers(data=form_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({'message':'Data saved succesfully!!'},status=200)
        else:
            return JsonResponse({'error':'oops something went wrong!!'},status=400)

# api logic for delete or update a particular employee from modal
@csrf_exempt
def UpdateDeleteView(request,id):
    try :
        get_employee=Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({'error':'please pass id as a parameter in url!!'},status=404)
    if request.method  == 'PUT':
        request_data=request.body
        stream = io.BytesIO(request_data)
        form_data=JSONParser().parse(stream)
        serialized_data=EmployeeSerializers(get_employee,data=form_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({'message':'Data updated succesfully!!'},status=200)
        else:
            return JsonResponse({'error':'oops something went wrong!!'},status=400)
    elif request.method == 'DELETE':
        get_employee.delete()
        return JsonResponse({'message':'Deleted!!'},status=200)


