from django.urls import path
from . import views
urlpatterns=[
    path('',views.add_employee),
    path('add_employee/',views.add_employee,name='add_employee'),
    path('view_employee/',views.view_employee,name='view_employee'),
    path('view_edit_or_delete_emp/',views.view_edit_or_delete_emp,
    name='view_edit_or_delete_emp'),
    path('delete_emp/<pk>',views.delete_emp,name='delete_emp'),
    path('edit_emp/<pk>',views.edit_emp,name='edit_emp')
    
]