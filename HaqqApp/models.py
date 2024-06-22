from django.db import models

class Employer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    skillsRequired = models.CharField(max_length=255, blank=False)

    def get_skills_required(self):
        return self.skills.split(',')

    def set_skills_required(self, skills):
        self.skills = ','.join(skills)


class Refugee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    skills = models.CharField(max_length=255, blank = False)

    def get_skills(self):
        return self.skills.split(',')

    def set_skills(self, skills):
        self.skills = ','.join(skills)