from api.v1 import views
from django.urls import path

urlpatterns = [
    path('generate/', views.CapibaraView.as_view()),
    path('statement/', views.CapibaraXlsxView.as_view()),
    path('statements/', views.CapibaraXlsxView.as_view()),
]
