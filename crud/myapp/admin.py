from django.contrib import admin
from myapp.models import Employee

# Register your models here.
@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display=['id','name','salary']