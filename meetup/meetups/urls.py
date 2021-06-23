from collections import namedtuple
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='all-meetups'),
    path('organizer-details',views.organization_details, name='organizer-details'),
    path('<slug:meetup_slug>/success',views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>',views.meetup_details, name='meetup-details')
]
