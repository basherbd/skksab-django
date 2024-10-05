from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm


# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_month = form.cleaned_data['month']
      new_saving = form.cleaned_data['saving']
      new_profit = form.cleaned_data['profit']
      new_withdraw = form.cleaned_data['withdraw']
      new_total = form.cleaned_data['total']
      new_install = form.cleaned_data['install']
      new_install_no = form.cleaned_data['install_no']
      new_install_due = form.cleaned_data['install_due']
      new_date = form.cleaned_data['date']
      new_remark = form.cleaned_data['remark']

      new_student = Student(
        month=new_month,
        saving=new_saving,
        profit=new_profit,
        withdraw=new_withdraw,
        total=new_total,
        install=new_install,
        install_no=new_install_no,
        install_due=new_install_due,
        date=new_date,
        remark=new_remark
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))
