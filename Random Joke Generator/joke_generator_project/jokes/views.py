import requests
from django.shortcuts import render

def random_joke(request):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    joke = response.json()['value']
    return render(request, 'jokes/random_joke.html', {'joke': joke})
