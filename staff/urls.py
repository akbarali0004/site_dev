from django.urls import path
from .views import staff_list, staff_form, update_staff, delete_staff, staff_view

urlpatterns = [
    path('', staff_list, name='staff_list'),
    path('create/', staff_form, name="create"),
    path('update/<int:pk>', update_staff, name="update-staff"),
    path('delete/<int:pk>', delete_staff, name="delete"),
    path('satff_view/<int:pk>', staff_view, name="staff-view"),
]