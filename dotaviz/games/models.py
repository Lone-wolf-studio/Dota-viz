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
    game_date = models.DateTimeField(editable=False)

    def __str__(self):
    	return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(Games, self).save(*args, **kwargs)	

# Tournaments
class Tournaments(models.Model):
	name = models.CharField(max_length=200)
	game = models.ForeignKey(Games, limit_choices_to={'match_type': GAME_MODE_CHOICES[1]})

	def __str__(self):
		return self.name    
