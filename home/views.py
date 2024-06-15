from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"index.html")
# Create your views here.

from django.shortcuts import render, redirect
from .forms import QuestionForm

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')  # Redirect to a success page
    else:
        form = QuestionForm()

    return render(request, 'add_question.html', {'form': form})

def explore(request):
    return render(request,"explore.html")

def index(request):
    return render(request, 'index.html')