from django.urls import path
from aimfit_app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.loginview,name='login'),
    path('trainer_register',views.trainer_register,name='trainer_register'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('trainer_view',views.trainer_view,name='trainer_view'),
    path('trainer_delete/<int:id>', views.trainer_delete, name='trainer_delete'),
    path('physician_register',views.physician_register,name='physician_register'),
    path('physician_delete/<int:id>', views.physician_delete, name='physician_delete'),
    path('physician_view',views.physician_view,name='physician_view'),
    path('add_equipments',views.add_equipments,name='add_equipments'),
    path('equipments_view',views.equipments_view,name='equipments_view'),
    path('equipments_delete/<int:id>',views.equipments_delete,name='equipments_delete'),
    path('user_home',views.user_home,name='user_home'),
    path('usertrainer_view',views.usertrainer_view,name='usertrainer_view'),
    path('userphysician_view', views.userphysician_view, name='userphysician_view'),
    path('userequip_view', views.userequip_view, name='userequip_view'),
    path('customer_register',views.customer_register,name='customer_register'),
    path('add_batch',views.add_batch,name='add_batch'),
    path('batch_view',views.batch_view,name='batch_view'),
    path('batch_delete/<int:id>', views.batch_delete, name='batch_delete'),
    path('batch_update/<int:id>', views.batch_update, name='batch_update'),
    path('add_complaint',views.add_complaint,name='add_complaint'),
    path('complaint_view',views.complaint_view,name='complaint_view'),
    path('usercomplaint_view',views.usercomplaint_view,name='usercomplaint_view'),
    path('complaint_reply/<int:id>', views.complaint_reply, name='complaint_reply'),
    path('add_Dietplan',views.add_Dietplan,name='add_Dietplan'),
    path('dietplan_view', views.dietplan_view, name='dietplan_view'),
    path('dietplan_delete/<int:id>', views.dietplan_delete, name='dietplan_delete'),
    path('userdietplan_view', views.userdietplan_view, name='userdietplan_view'),
    path('customer_view',views.customer_view,name='customer_view'),
    path('customer_delete/<int:id>', views.customer_delete, name='customer_delete'),
    path('add_attendence',views.add_attendence,name='add_attendence'),
    path('mark_attendence/<int:id>', views.mark_attendence, name='mark_attendence'),
    path('view_attendence/',views.view_attendence,name='view_attendence'),
    path('day_attendence/<date>/', views.day_attendence, name='day_attendence'),
    path('add_health',views.add_health,name='add_health'),
    path('health_view',views.health_view,name='health_view'),
    path('trainer_custview', views.trainer_custview, name='trainer_custview'),
    path('update_health/<int:id>', views.update_health, name='update_health'),
    path('delete_health/<int:id>', views.delete_health, name='delete_health'),
    path('trainer_home',views.trainer_home,name='trainer_home'),
    path('add_Notification',views.add_Notification,name='add_Notification'),
    path('notif_view/',views.notif_view,name='notif_view'),
    path('notification_update/<int:id>', views.notification_update, name='notification_update'),
    path('notification_delete/<int:id>', views.notification_delete, name='notification_delete'),
    path('usernotif_view', views.usernotif_view, name='usernotif_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('add_payment',views.add_payment,name='add_payment'),
    path('payment_view',views.payment_view,name='payment_view'),
    path('user_payview',views.user_payview,name='user_payview'),
    path('add_card/<int:id>',views.add_card,name='add_card'),
    path('cardpay_view',views.cardpay_view,name='cardpay_view'),
    path('profile_view', views.profile_view, name='profile_view'),
    path('profile_update/<int:id>', views.profile_update, name='profile_update'),


]