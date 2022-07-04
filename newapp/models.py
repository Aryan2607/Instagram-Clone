from distutils.log import info
from email.headerregistry import Address
from email.policy import default
from pickle import TRUE
from time import time
from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.
class student(models.Model):
    Name = models.CharField(max_length=40, null=TRUE)
    Email = models.EmailField(null = TRUE)
    Roll_no = models.PositiveIntegerField(null=TRUE)
    Address = models.TextField(null=TRUE)
    Image = models.ImageField(null=TRUE)
    def __str__(Self):
        return Self.Name

    # def __str__(Event.objects.get(student__Name='1')) #this is another filter
    # def __str__(Event.objects.get(Name__stratswith='A'))
    

department_choices = (
        ("1","HR"),
        ("2","Software"),
        ("3","Marketing"),
    )

class Employee(models.Model):
    emp_name = models.CharField(max_length=40)
    emp_id = models.PositiveIntegerField()
    is_active = models.BooleanField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    department = models.CharField(max_length=20, choices=department_choices)
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    time = models.TimeField(auto_now_add=True ,null=True)
    created_at = models.DateTimeField(null=True, default=timezone.now)
    updated_at = models.DateTimeField(null=True, default=timezone.now, blank=True)
    # name = models.ForeignKey(student,on_delete=models.CASCADE, null=True)
    info = models.ManyToManyField("student", related_name=("Employee"))
    
    def __str__(Self):
        return Self.emp_name
