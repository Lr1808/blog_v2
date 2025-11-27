from django.urls import path
from .views import (
                    PublicationListView, 
                    PublicationCreteView,
                    PublicationDetailView,
                    PublicationUpdateView,
                    PublicationDeleteView
                  )                   

urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
    path('publication/new/', PublicationCreteView.as_view(), name='publications-create'),
    path('publication/<int:pk>/', PublicationDetailView.as_view(), name='publications-detail'),
    path('publication/<int:pk>/edit/', PublicationUpdateView.as_view(), name='publications-update'),
    path('publication/<int:pk>/delete/', PublicationDeleteView.as_view(), name='publications-delete'),
]
