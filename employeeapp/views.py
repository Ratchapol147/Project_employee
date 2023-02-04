from django.shortcuts import render,redirect
from django.http import HttpResponse
from employeeapp.forms import EmployeeForm
from employeeapp.models import employee
import os
from django.conf import settings

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        all_employee = employee.objects.filter(fname__contains=name,lname__contains=name)
        return render(request,'index.html',{'all_employee':all_employee,'name':name})
    else:
        all_employee = employee.objects.all()
        return render(request,'index.html',{'all_employee':all_employee})

def create(request):
    if request.method == 'POST':
        #บันทึกข้อมูล
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('/')
    else :
        form = EmployeeForm()
        return render(request,'create.html',{'form':form})

def delete(request,emp_id):
    emp = employee.objects.get(pk = emp_id)
    emp.delete()
    return redirect('/')

def edit(request,emp_id):
    #อัพเดทข้อมูล
    if request.method =='POST':
        emp = employee.objects.get(pk=emp_id)
        form = EmployeeForm(request.POST, request.FILES,instance=emp)
        if form.is_valid():
            image_path = emp.cover.path
            if os.path.exists(image_path):
                os.delete(image_path)
            form.save()
            return redirect('/')
    #แก้ไขข้อมูล
    else:
        #ดึงข้อมูลพนักงานที่ต้องแก้
        emp = employee.objects.get(pk=emp_id)
        #โยนข้อมูลเข้าแบบฟอร์มแก้ไข
        form = EmployeeForm(initial=emp.__dict__)
        return render(request,'edit.html',{'form':form})
    
