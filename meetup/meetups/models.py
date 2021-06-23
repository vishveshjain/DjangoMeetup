from django.db import models
from django.db.models.base import Model
from django.core.validators import RegexValidator


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'{self.name} ({self.address})'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email

class Organizer(models.Model):
    orgName = models.CharField(max_length=100)
    orgEmail = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.")
    orgContact = models.CharField(validators=[phone_regex], max_length=11)
    orgDate = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.orgName}'

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to ='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participant = models.ManyToManyField(Participant, blank=True, null=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title} - {self.slug}'


