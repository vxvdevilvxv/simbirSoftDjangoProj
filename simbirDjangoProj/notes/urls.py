from django.urls import path
from .views import index, register, login_user, add_note, user_logout, view_notes

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_note/', add_note, name='add_note'),
    path('view_notes/', view_notes, name='view_notes'),

]
