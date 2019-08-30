from django.urls import path
from sourcebook import views
from .views import PageView, SourceUpdateView


app_name = 'sourcebook'
urlpatterns = [
    path('', views.index, name='Index'),
    path('book/<int:book>/', views.book, name='Book'),
    path('book/<int:book>/page/<int:page>/', PageView.as_view(), name='Page'),
    path('book/<int:book>/page/<int:page>/update/<int:source>', SourceUpdateView.as_view(), name='Source_Update'),
    
]