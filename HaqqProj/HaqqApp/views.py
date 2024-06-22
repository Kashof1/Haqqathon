from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .forms import EmployerSignUpForm, RefugeeSignUpForm, SkillSearchForm
from .models import Employer, Refugee

class EmployerSignupView(FormView):
    template_name = 'employer_signup.html'
    form_class = EmployerSignUpForm
    success_url = '/'

    def form_valid(self, form):
        # Save the new employer to the database
        form.save()
        return super().form_valid(form)


class RefugeeSignupView(FormView):
    template_name = 'refugee_signup.html'
    form_class = RefugeeSignUpForm
    success_url = '/'

    def form_valid(self, form):
        # Save the new employer to the database
        form.save()
        return super().form_valid(form)
class HomeView(FormView):
    template_name = 'home.html'
    form_class = SkillSearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SkillSearchForm()
        context['refugees'] = None
        return context

    def post(self, request, *args, **kwargs):
        print("POSTED")
        form = SkillSearchForm(request.POST)
        if form.is_valid():
            skill = form.cleaned_data['skill']
            refugees = Refugee.objects.filter(skills__icontains=skill)
            print('refugees ', refugees)
            return self.render_to_response(self.get_context_data(form=form, refugees=refugees))
        return self.render_to_response(self.get_context_data(form=form))