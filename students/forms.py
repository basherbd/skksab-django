from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['month', 'saving', 'profit', 'withdraw', 'total', 'install', 'install_no', 'install_due', 'date', 'remark']
    labels = {
      'month': 'Month',
      'saving': 'Saving',
      'profit': 'Profit',
      'withdraw': 'Withdraw',
      'total': 'Total',
      'install': 'Install',
      'install_no': 'Install No',
      'install_due': 'Install Due',
      'date': 'Date',
      'reemark': 'Remark'
    }
    widgets = {
      'month': forms.TextInput(attrs={'class': 'form-control'}),
      'saving': forms.TextInput(attrs={'class': 'form-control'}),
      'profit': forms.TextInput(attrs={'class': 'form-control'}),
      'withdraw': forms.TextInput(attrs={'class': 'form-control'}),
      'total': forms.TextInput(attrs={'class': 'form-control'}),
      'loan': forms.TextInput(attrs={'class': 'form-control'}),
      'install': forms.TextInput(attrs={'class': 'form-control'}),
      'install_no': forms.NumberInput(attrs={'class': 'form-control'}),
      'install_due': forms.TextInput(attrs={'class': 'form-control'}),
      'date': forms.TextInput(attrs={'class': 'form-control'}),
      'remark': forms.TextInput(attrs={'class': 'form-control'}),
    }
