from .forms import RegistrationForm
from django.db.models.fields import URLField
from django.shortcuts import redirect, render
from .models import Location, Meetup, Participant

# Create your views here.

def index(request):
    meetups= Meetup.objects.all()
    return render(request,'meetups/index.html',
        {
            'show_meetups':True,
            'meetups':meetups
        }
    )

def meetup_details(request, meetup_slug):
    try:
        selected_meetup =Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participants, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participant.add(participants)
                return redirect('confirm-registration',meetup_slug=meetup_slug)
        return render(request,'meetups/meetup-details.html',
            {
                'meetup_found':True,
                'meetup_title':selected_meetup.title,
                'meetup_description':selected_meetup.description,
                'meetup_location' : selected_meetup.location.address,
                'meetup_image': selected_meetup.image.url,
                'form': registration_form,
                'slug' : selected_meetup.slug
            })
    except Exception as ex:
        return render(request,'meetups/meetup-details.html',
        {
            'meetup_found':False
        })

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html')


def organization_details(request):
    meetups= Meetup.objects.all()
    return render(request,'meetups/organizer-details.html',
        {
            'meetups':meetups
        })