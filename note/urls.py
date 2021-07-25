from django.urls import path
from note.views import createNotes, dashBoard, updateNotes, deleteTask


urlpatterns = [
    # path('home/', homePage, name='home'),
    path('dashboard/', dashBoard, name='dashboard'),
    path('create/', createNotes, name='create'),
    path('update/<str:pk>/', updateNotes, name='update'),
    path('delete/<str:pk>/', deleteTask, name='delete')
]