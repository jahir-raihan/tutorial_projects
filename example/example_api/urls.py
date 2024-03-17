from django.urls import path
from .views import ExampleAPIView

urlpatterns = [
    path('book', ExampleAPIView.as_view(), name='example_view')
]