from collections import namedtuple
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='all-meetups'),
    path('<slug:meetup_slug>',views.meetup_details, name='meetup-details'),
    path('<slug:organizer_slug>/organizer-details',views.organization_details, name='organizer-details'),
    path('<slug:registration_slug>/success',views.confirm_registration, name='confirm-registration')
]
