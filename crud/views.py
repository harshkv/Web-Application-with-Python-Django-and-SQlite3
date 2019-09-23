from django.shortcuts import render, redirect
from crud.forms import EmployeeForm,EducationForm
from crud.models import Employee,Education
from django.contrib.auth.decorators import login_required
from django.views import View
#
# def create(request):
#     form = EmployeeForm()
#     if request.method =='POST' :
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, 'crud/create.html',{'form':form})

# Create your views here.
#this is for AJAX
# def load_data(request):
#     resultSet = Employee.objects.filter().values()
#     return JsonResponse(list(resultSet),safe =False)

def create(request):
    form = EmployeeForm()
    if request.method =='POST' :
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp = Employee()
            empName = form.cleaned_data['emp_email'].split('@')[0]
            emp.emp_name = empName
            emp.emp_email = form.cleaned_data['emp_email']
            emp.address = form.cleaned_data['address']
            emp.phone = form.cleaned_data['phone']
            emp.save()
            return redirect(index)


    return render(request, 'crud/create.html',{'form':form})



@login_required(login_url = '/sites/login')
def index(request):
    resultSet = Employee.objects.all()
    # resultSet = Employee.objects.filter(emp_name = 'tst')
    # resultSet = Employee.objects.order_by('-id')
    # resultSet = Employee.objects.filter(emp_name = 'tst').values('id','emp_name')
    # resultSet = Employee.objects.raw(" ")
    return render(request, 'crud/index.html', {'data':resultSet})

def update(request,id):
    data = Employee.objects.get(id=id)
    #select * from employee where id==id

    form = EmployeeForm(instance = data)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance = data)
        if form.is_valid():
            emp = Employee()
            emp.id =id
            empName = form.cleaned_data['emp_name'].split('@')[0]
            emp.emp_name = empName
            emp.emp_email = form.cleaned_data['emp_email'] 
            emp.address = form.cleaned_data['address']
            emp.phone = form.cleaned_data['phone']
            emp.save()
            return redirect(index)
    return render(request, 'crud/update.html', {'form': form})


def delete(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect(index)



def view(request,id):
    data = Employee.objects.get(id=id)
    return render (request,'crud/view.html',{'data':data})


def edu_Create(request):
    form = EducationForm()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            edu = Education()
            edu.edu_name = form.cleaned_data['edu_name']
            edu.edu_type = form.cleaned_data['edu_type']
            edu.edu_uni  = form.cleaned_data['edu_uni']
            edu.employee = form.cleaned_data['employee']
            edu.save()
            return redirect(edu_Index)
    return render(request,'education/eduCreate.html',{'form': form})

# @login_required(login_url = '/sites/login')
def edu_Index(request):
    resultSet = Education.objects.all()
    return render(request,'education/eduIndex.html',{'data':resultSet})


def edu_Update(request,id):
    data = Education.objects.get(id=id)
    form = EducationForm(instance = data)
    if request.method == 'POST':
        form = EducationForm(request.POST,instance = data)
        if form.is_valid():
            edu = Education()
            edu.edu_name = form.cleaned_data['edu_name']
            edu.edu_type = form.cleaned_data['edu_type']
            edu.edu_uni = form.cleaned_data['edu_uni']
            edu.employee = form.cleaned_data['employee']
            edu.save()
            return redirect(edu_Index)
    return render(request, 'education/eduUpdate.html',{'form':form})



def edu_Delete(request, id):
    data = Education.objects.get(id=id)
    data.delete()
    return redirect(edu_Index)



def edu_View(request,id):
    data = Education.objects.get(id=id)
    return render (request,'education/eduView.html',{'data':data})


class CreateView(View):
    def get(self,request):
        print('ASd')
        form = EmployeeForm()
        return render(request,'crud/create.html', {'form':form})
    def post(self,request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        return render(request, 'crud/create.html', {'form': form})