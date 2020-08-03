from django.shortcuts import render, render_to_response
from characters.models import DotaCharacters
from django.template import RequestContext

def heroes(request, template='gamecharacters/heroes.html'):
	heroes_list = DotaCharacters.objects.all()
	context = {
	'heroes_list' : heroes_list
	}	
	return render(request, template, context)