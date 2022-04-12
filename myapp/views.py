from django.shortcuts import render
from .forms import ResumeForm, ContactUsModalForm
from .models import Resume
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.
class HomeView(View):

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data['name'])
            form.save()
            return render(request, 'home.html', {'form': form})

    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        context = {'form': form,
                   'candidates': candidates}
        return render(request, 'home.html', context)


class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'employee.html', {'candidate': candidate})


class ContactView(View):
    def get(self, request):
        form = ContactUsModalForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactUsModalForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': form})
