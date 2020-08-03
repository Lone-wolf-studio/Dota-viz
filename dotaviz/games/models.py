from django.db import models
from django.contrib.models import User
from characters.models import DotaCharacters

GAME_MODE_CHOICES = (
	('A','All Pick'),
	('T', 'Turbo'),
	('S', 'Single Draft'),
	('C', 'Captains Mode'),
	('R', 'Random Draft'),
	('L', 'Least Played')
	)

REGION_CHOICES = (
	('UW','US West'),
	('UE','US East'),
	('EW','Europe West'),
	('EE','Europe East'),
	('RU','Russia'),
	('SA','SE Asia'),
	('AU','Australia'),
	('AS','South America'),
	('DU','Dubai'),
	('CH','Chile'),
	('PE','Peru'),
	('AF','South Africa'),
	('IN','India'),
	('JA','Japan'),
	('CH','China UC')
	)

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User)
    heroes = models.ManyToManyField(DotaCharacters)
    region = models.CharField(max_length=1, choices=REGION_CHOICES)
    match_type = models.CharField(max_length=2, choices=GAME_MODE_CHOICES)

    def __str__(self):
    	return self.name
