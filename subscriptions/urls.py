from django.urls import path 

from .views import PackageView,SubscriptiomView

urlpatterns=[
    path('packages/',PackageView.as_view()),
    path('subscriptions/',SubscriptiomView.as_view())
    
]