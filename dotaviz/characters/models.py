from django.db import models

HERO_TYPE_CHOICES = (
        ('S', 'Strength'),
        ('A', 'Agility'),
        ('I', 'Intelligence')
    )

# Create your models here.
class DotaCharacters(models.Model):
	name = models.CharField(max_length=200)
	hero_type = models.CharField(max_length=1, choices=HERO_TYPE_CHOICES)
	character_img = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name