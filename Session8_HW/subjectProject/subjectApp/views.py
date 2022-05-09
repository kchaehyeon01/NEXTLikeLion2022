from django.shortcuts import render
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    majors = Major.objects.all()

    return render(request, 'home.html', {'majors' : majors})

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')