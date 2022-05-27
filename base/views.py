from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Lets learn Django'},
    {'id': 3, 'name': 'Lets learn Flask'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')