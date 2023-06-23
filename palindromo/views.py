from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def es_palindromo(s):
    s = s.lower().replace(' ', '')
    rev = ''.join(reversed(s))
    return s == rev

def palindromo(request, word):
    if es_palindromo(word):
        response = f"{word} ES PALINDROMO"
    else:
        response = f"{word} NO ES PALINDROMO"
    return HttpResponse(response)
