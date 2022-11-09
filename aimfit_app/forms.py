import payment as payment
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import DateInput

from aimfit_app.models import Login, Trainer, Physician, Equipments, Customer, Batch, Complaint, Dietplan, Attendence, \
    Health, Notification, Payment


class TimeInput(forms.TimeInput):
    input_type = 'time'


class DateInput(forms.DateInput):
    input_type = 'date'


class LoginForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ('name', 'age', 'address', 'qualification', 'achievement', 'contact_no', 'image')


class physicianForm(forms.ModelForm):
    class Meta:
        model = Physician
        fields = ('name', 'age', 'address', 'qualification', 'contact_no', 'image')


class EquipmentsForm(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = ('name', 'image', 'description')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'age', 'address', 'contact_no', 'image')


class BatchForm(forms.ModelForm):
    time: forms.TimeInput(attrs={'type': 'time'})

    class Meta:
        model = Batch
        fields = ('name', 'time')


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('complaint',)


class ComplaintForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Complaint
        fields = ('complaint', 'date')


class DietplanForm(forms.ModelForm):
    class Meta:
        model = Dietplan
        fields = ('subject', 'image')


class Attendence(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Attendence
        fields = ('name', 'attendence', 'date', 'time')


class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ('name', 'height', 'weight', 'healthcondition', 'medicineconsumption')


class NotificationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Notification
        fields = ('date', 'subject', 'description')


class PaymentForm(forms.ModelForm):
    due_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Payment
        fields = ('name','amount', 'due_date')


