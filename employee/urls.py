# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login', views.login),
#     path('register', views.register),
#     path('findByEmail', views.find_by_email),
#     path('getAll', views.get_all),
#     path('getById', views.get_by_id),
#     path('update', views.update),
#     path('delete', views.delete),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.get_all, name='get_all_employees'),   # ✅ GET all employees
    path('employee/<int:id>/', views.get_by_id, name='get_by_id'), # ✅ GET by ID
    path('employee/add/', views.register, name='register_employee'),
    path('employee/update/', views.update, name='update_employee'),
    path('employee/delete/', views.delete, name='delete_employee'),
    path('employee/login/', views.login, name='login_employee'),
    path('employee/find/', views.find_by_email, name='find_by_email'),
]



