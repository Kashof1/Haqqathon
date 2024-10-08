from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .forms import EmployerSignUpForm, RefugeeSignUpForm, SkillSearchForm
from .models import Employer, Refugee
from HaqqApp.core.utils import find_keys, get_score
import os
import json

#defining path for labels stored in core/labels.json for use in the HomeView
pathtolabels = os.path.join('HaqqApp', 'core', 'labels.json')


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = SkillSearchForm()
    #     context['refugees'] = None
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SkillSearchForm()
        context['refugees'] = kwargs.get('refugees', None)
        context['refugees'] = None
        return context

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        with open(pathtolabels, 'r') as f:
            labels = json.load(f)

        form = SkillSearchForm(request.POST)
        if form.is_valid():
            targetSkill = form.cleaned_data['skill']
            refugees = Refugee.objects.all()

            refugeescores = []
            for each in refugees:
                eachSkills = each.skills
                score = get_score(skills=eachSkills, target=targetSkill, data=labels)
                if score == 1:
                    rating = "Strong match"
                elif score == 2:
                    rating = "Mediocre match"
                elif score == 3:
                    rating = "Weak match"
                else:
                    rating = "No significant match"
                refugeescores.append([each, rating, score])

            sortedRefugees = sorted(refugeescores, key=lambda x: x[2], reverse=False)[:5] #top 5 refugee matches
            sortedRefugees = [each for each in sortedRefugees if each[2] != float('inf')]
            context['refugees'] = sortedRefugees
            print(f"sorted refugees : {sortedRefugees}")
            print(f"context : {context['refugees']}")

            #return self.render_to_response(self.get_context_data(form=form, refugees=sortedRefugees))
        #return self.render_to_response(self.get_context_data(form=form))
            return render(request, 'home.html', context)