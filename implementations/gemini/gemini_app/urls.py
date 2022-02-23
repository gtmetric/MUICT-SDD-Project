from django.urls import path
from .views import (
    home,
    create_success,
    SciencePlanCreateView,
    TestSciencePlanListView,
    TestSciencePlanUpdateView,
    ValidateSciencePlanListView,
    ValidateSciencePlanDetailView
)


urlpatterns = [
    path('', home, name='home'),
    path('create/', SciencePlanCreateView.as_view(), name='create'),
    path('create/success/', create_success, name='create-success'),
    path('test/', TestSciencePlanListView.as_view(), name='test'),
    path('test/<int:pk>/', TestSciencePlanUpdateView.as_view(), name='test-detail'),
    path('validate/', ValidateSciencePlanListView.as_view(), name='validate'),
    path('validate/<int:pk>/', ValidateSciencePlanDetailView.as_view(), name='validate-detail'),
]
