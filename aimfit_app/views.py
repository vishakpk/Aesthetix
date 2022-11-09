import datetime

import payment
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from requests import request

from aimfit_app.models import Trainer, Login, Physician, Equipments, Batch, Complaint, Dietplan, Customer, Attendence, \
    Health, Notification, Payment

# Create your views here.
from aimfit_app.forms import LoginForm, TrainerForm, physicianForm, EquipmentsForm, CustomerForm, BatchForm, \
    ComplaintForm, DietplanForm, HealthForm, NotificationForm, PaymentForm


def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_trainer:
                return redirect('trainer_home')
            elif user.is_user:
                return redirect('student_home')
            elif user.is_physician:
                return redirect('physician_home')
            elif user.is_customer:
                return redirect('user_home')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'login.html')


#############ADMINTEMP##########################

def admin_home(request):
    return render(request, 'admintemp/admin_home.html')


def trainer_register(request):
    login_form = LoginForm()
    trainer_form = TrainerForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        trainer_form = TrainerForm(request.POST, request.FILES)
        if login_form.is_valid() and trainer_form.is_valid():
            user = login_form.save(commit=False)
            user.is_trainer = True
            user.save()
            trainer = trainer_form.save(commit=False)
            trainer.user = user
            trainer.save()
            messages.info(request, 'Registration Successful')
            return redirect('trainer_view')
    return render(request, 'admintemp/trainer_register.html', {'login_form': login_form, 'trainer_form': trainer_form})


def trainer_view(request):
    register = Trainer.objects.all()
    return render(request, 'admintemp/trainer_view.html', {'register': register})


def trainer_delete(request, id):
    data = Trainer.objects.get(id=id)
    data1 = Login.objects.get(trainer=data)
    if request.method == "POST":
        data1.delete()
        return redirect('trainer_view')
    else:
        return redirect('trainer_view')


def physician_register(request):
    login_form = LoginForm()
    physician_form = physicianForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        physician_form = physicianForm(request.POST, request.FILES)
        if login_form.is_valid() and physician_form.is_valid():
            user = login_form.save(commit=False)
            user.is_physician = True
            user.save()
            physician = physician_form.save(commit=False)
            physician.user = user
            physician.save()
            messages.info(request, 'Registration Successful')
            return redirect('physician_view')
    return render(request, 'admintemp/physician register.html',
                  {'login_form': login_form, 'physician_form': physician_form})


def physician_view(request):
    register = Physician.objects.all()
    return render(request, 'admintemp/physician_view.html', {'register': register})


def physician_delete(request, id):
    data = Physician.objects.get(id=id)
    data1 = Login.objects.get(physician=data)
    if request.method == "POST":
        data1.delete()
        return redirect('physician_view')
    else:
        return redirect('physician_view')


def add_equipments(request):
    equipment_form = EquipmentsForm()
    if request.method == 'POST':
        equipment_form = EquipmentsForm(request.POST, request.FILES)
        if equipment_form.is_valid:
            equipment = equipment_form.save()
            equipment.save()
            messages.info(request, 'Equipment Added Successful')
        return redirect('equipments_view')
    return render(request, 'admintemp/add_equipments.html', {'equipment_form': equipment_form})


def equipments_view(request):
    equipments = Equipments.objects.all()
    return render(request, 'admintemp/equipments_view.html', {'equipments': equipments})


def equipments_delete(request, id):
    data = Equipments.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('equipments_view')
    else:
        return redirect('equipments_view')


def user_home(request):
    return render(request, 'usertemp/user_home.html')


def usertrainer_view(request):
    register = Trainer.objects.all()
    return render(request, 'usertemp/usertrainer_view.html', {'register': register})


def userphysician_view(request):
    register = Physician.objects.all()
    return render(request, 'usertemp/userphysician_view.html', {'register': register})


def userequip_view(request):
    equipments = Equipments.objects.all()
    return render(request, 'usertemp/userequip_view.html', {'equipments': equipments})


def customer_register(request):
    login_form = LoginForm()
    customer_form = CustomerForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        customer_form = CustomerForm(request.POST, request.FILES)
        if login_form.is_valid() and customer_form.is_valid():
            user = login_form.save(commit=False)
            user.is_customer = True
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            messages.info(request, 'Registration Successful')
            return redirect('login')
    return render(request, 'Register.html',
                  {'login_form': login_form, 'customer_form': customer_form})


def add_batch(request):
    batch_form = BatchForm()
    if request.method == 'POST':
        batch_form = BatchForm(request.POST)
        # print(batch_form)
        if batch_form.is_valid():
            batch_form.save()
            messages.info(request, 'Batch Added Successful')
            return redirect('batch_view')
    return render(request, 'admintemp/add_batch.html', {'batch_form': batch_form})


def batch_view(request):
    batch = Batch.objects.all()
    return render(request, 'admintemp/batch_view.html', {'batch': batch})


def batch_delete(request, id):
    data = Batch.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('batch_view')
    else:
        return redirect('batch_view')


def batch_update(request, id):
    data = Batch.objects.get(id=id)
    if request.method == 'POST':
        form = BatchForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, 'Batch update Succesfully')
            return redirect('batch_view')
    else:
        form = BatchForm(instance=data)
    return render(request, 'admintemp/batch_update.html', {'form': form})


def add_complaint(request):
    complaint_form = ComplaintForm()
    if request.method == 'POST':
        complaint_form = ComplaintForm(request.POST, request.FILES)
        if complaint_form.is_valid:
            complaint = complaint_form.save()
            complaint.save()
            messages.info(request, 'complaint send Successful')
        return redirect('user_home')
    return render(request, 'usertemp/add_complaint.html', {'Complaint_form': complaint_form})


def complaint_view(request):
    complaint = Complaint.objects.all()
    return render(request, 'admintemp/complaint_view.html', {'complaint': complaint})


def usercomplaint_view(request):
    complaint = Complaint.objects.all()
    return render(request, 'usertemp/usercomplaint_view.html', {'complaint': complaint})


def add_complaint(request):
    complaint_form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        complaint_form = ComplaintForm(request.POST)
        if complaint_form.is_valid():
            obj = complaint_form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Comlaint Added Successful')
            return redirect('usercomplaint_view')
    return render(request, 'usertemp/add_complaint.html', {'complaint_form': complaint_form})


def usercomplaint_view(request):
    complaint = Complaint.objects.filter(user=request.user)
    return render(request, 'usertemp/usercomplaint_view.html', {'complaint': complaint})


def complaint_reply(request, id):
    print("heloo")
    rid = Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        rid.reply = r
        rid.save()
        messages.info(request, 'Reply added Successfuly')
        return redirect('complaint_view')
    return render(request, 'admintemp/complaint_reply.html', {'rid': rid})


def complaint_view(request):
    complaint2 = Complaint.objects.all()
    return render(request, 'admintemp/complaint_view.html', {'complaint2': complaint2})


def add_Dietplan(request):
    dietplan_Form = DietplanForm()
    if request.method == 'POST':
        dietplan_Form = DietplanForm(request.POST, request.FILES)
        if dietplan_Form.is_valid:
            dietplan = dietplan_Form.save()
            dietplan.save()
            messages.info(request, 'Dietplan Added Successful')
        return redirect('dietplan_view')
    return render(request, 'trainertemp/add_Dietplan.html', {'dietplan_Form': dietplan_Form})


def dietplan_view(request):
    dietplan = Dietplan.objects.all()
    return render(request, 'trainertemp/dietplan_view.html', {'dietplan': dietplan})


def dietplan_delete(request, id):
    data = Dietplan.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('dietplan_plan')
    else:
        return redirect('dietplan_plan')


def userdietplan_view(request):
    dietplan = Dietplan.objects.all()
    return render(request, 'usertemp/dietplan_view.html', {'dietplan': dietplan})


def customer_view(request):
    customer = Customer.objects.all()
    return render(request, 'usertemp/customer_view.html', {'customer': customer})


def customer_delete(request, id):
    data = Customer.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('customer_view')
    else:
        return redirect('customer_view')


def add_attendence(request):
    customer = Customer.objects.all()
    return render(request, 'admintemp/add_attendence.html', {'customer': customer})


now = datetime.datetime.now()


def mark_attendence(request, id):
    user = Customer.objects.get(user_id=id)
    att = Attendence.objects.filter(name=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, "today's attendence already marked for this student")
        return redirect('add_attendence')
    else:
        if request.method == 'POST':
            attendence = request.POST.get('attendence')
            Attendence(name=user, date=datetime.date.today(), attendence=attendence, time=now.time()).save()
            messages.info(request, "attendence added successfully")
            return redirect('add_attendence')
        return render(request, 'admintemp/mark_attendence.html')


def view_attendence(request):
    value_list = Attendence.objects.values_list('date', flat=True).distinct()
    attendence = {}
    for value in value_list:
        attendence[value] = Attendence.objects.filter(date=value)
    return render(request, 'admintemp/view_attendence.html', {'attendences': attendence})


def day_attendence(request, date):
    attendence = Attendence.objects.filter(date=date)
    context = {
        'attendence': attendence,
        'date': date
    }
    return render(request, 'admintemp/day_attendence.html', context)


def add_health(request):
    health_form = HealthForm()
    if request.method == 'POST':
        health_form = HealthForm(request.POST)
        if health_form.is_valid():
            health_form.save()
        messages.info(request, 'health condition is updated')
        return redirect('health_view')
    return render(request, 'trainertemp/add_health.html', {'health_form': health_form})


def health_view(request):
    health = Health.objects.all()
    return render(request, 'trainertemp/health_view.html', {'health': health})


def trainer_custview(request):
    customer = Customer.objects.all()
    return render(request, 'trainertemp/trainer_custview.html', {'customer': customer})


def update_health(request, id):
    n = Health.objects.get(id=id)
    if request.method == 'POST':
        health_form = HealthForm(request.POST or None, instance=n)
        if health_form.is_valid():
            health_form.save()
            messages.info(request, 'Health updated successfully')
            return redirect('health_view')
    else:
        health_form = HealthForm(instance=n)
    return render(request, 'trainertemp/update_health.html', {'health_form': health_form})


def delete_health(request, id):
    data = Health.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('health_view')
    else:
        return redirect('health_view')


def trainer_home(request):
    return render(request, 'trainertemp/trainer_home.html')


def add_Notification(request):
    notification_form = NotificationForm()
    if request.method == 'POST':
        notification_form = NotificationForm(request.POST)
        if notification_form.is_valid():
            notification_form.save()
        messages.info(request, 'notification  is updated')
        return redirect('notif_view')
    return render(request, 'admintemp/add_notification.html', {'notification_form': notification_form})


def notif_view(request):
    notif = Notification.objects.all()
    return render(request, 'admintemp/notif_view.html', {'notif': notif})


def notification_update(request, id):
    data = Notification.objects.get(id=id)
    if request.method == 'POST':
        form = NotificationForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, 'notification update Succesfully')
            return redirect('notif_view')
    else:
        form = NotificationForm(instance=data)
    return render(request, 'admintemp/notification_update.html', {'form': form})


def notification_delete(request, id):
    data = Notification.objects.get(id=id)
    if request.method == "POST":
        data.delete()
        return redirect('notif_view')
    else:
        return redirect('notif_view')


def usernotif_view(request):
    notif = Notification.objects.all()
    return render(request, 'usertemp/usernotif_view.html', {'notif': notif})


def add_payment(request):
    payment_form = PaymentForm()
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_form.save()
            messages.info(request, 'payment done Successfully')
            return redirect('payment_view')
    return render(request, 'admintemp/add_payment.html', {'payment_form': payment_form})


def payment_view(request):
    payment = Payment.objects.all()
    return render(request, 'admintemp/view_payment.html', {'payment': payment})


def user_payview(request):
    pay = Payment.objects.filter(name=request.user.customer)
    return render(request, 'usertemp/user_payview.html', {'pay': pay})

def add_card(request,id):
    pay=Payment.objects.get(id=id)
    if request.method=='POST':
        c=request.POST.get('card_no')
        cn=request.POST.get('card_name')
        cvv=request.POST.get('cvv')
        pay.card_no=c
        pay.card_name=cn
        pay.cvv=cvv
        pay.save()
        messages.info(request,'Payment Done Successfully!')
        return redirect('cardpay_view')
    return render(request,'usertemp/add_card.html',{'pay':pay})


def cardpay_view(request):
    return render(request, 'usertemp/cardpay.html')

def profile_view(request):
    prof=Trainer.objects.all()
    return render(request,'trainertemp/profile_view.html',{'prof':prof})

def profile_update(request,id):
    data=Trainer.objects.get(id=id)
    if request.method=='POST':
        form=TrainerForm(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            messages.info(request,'Profile Updated Suuccessfully!')
            return redirect('profile_view')
    else:
        form=TrainerForm(instance=data)
        return render(request,'trainertemp/profile_update.html',{'form':form})