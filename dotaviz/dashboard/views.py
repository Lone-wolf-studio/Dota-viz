from django.shortcuts import render, render_to_response

# Create your views here.
def home_view(request, template='home.html'):
    return render_to_response(template)

