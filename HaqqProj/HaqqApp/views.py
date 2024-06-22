from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .forms import EmployerSignUpForm, RefugeeSignUpForm, SkillSearchForm
from .models import Employer, Refugee

class EmployerSignupView(FormView):
    template_name = 'employer_signup.html'
    form_class = EmployerSignUpForm
    success_url = '/'

class RefugeeSignupView(FormView):
    template_name = 'refugee_signup.html'
    form_class = RefugeeSignUpForm
    success_url = '/'

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SkillSearchForm()
        context['refugees'] = None
        return context

    def post(self, request, *args, **kwargs):
        form = SkillSearchForm(request.POST)
        if form.is_valid():
            skill = form.cleaned_data['skill']
            refugees = Refugee.objects.filter(skills__icontains=skill)
            return self.render_to_response(self.get_context_data(form=form, refugees=refugees))
        return self.render_to_response(self.get_context_data(form=form))