from django.urls import path
from .views import CurrentDateView, HelloWorld, RandomNumber


urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('hello/', HelloWorld.as_view()),
    path('random/', RandomNumber.as_view())
]
