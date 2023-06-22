from django.db import models

# Create your models here.
class About(models.Model):
    career_title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to ='profile/')

    def __str__(self):
        return(self.career_title)

class Skill(models.Model):
    skill_name = models.CharField(max_length = 80)
    percentage = models.IntegerField(null=False, blank=False, default = 0)

    def __str__(self):
        return(self.skill_name)

class Education(models.Model):
    title = models.CharField(max_length = 80)
    school_name = models.CharField(max_length = 80)
    description = models.CharField(max_length=200, blank=False, null=False)
    end_year = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return(self.school_name)

class Experience(models.Model):
    title = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    description = models.TextField(blank=False, null=False)
    emp_time = models.CharField(max_length = 80)

    def __str__(self):
        return(self.title)

class Project(models.Model):
    title = models.CharField(max_length = 200)
    project_img = models.ImageField(upload_to = 'project/')
    description = models.TextField(blank=False, null=False)
    git_url = models.URLField()
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return(self.title)

class Testimonal(models.Model):
    name = models.CharField(max_length = 200)
    title = models.CharField(max_length=250,blank=False)
    profile_img = models.ImageField(upload_to = 'testimonals/')
    recommendation = models.TextField(blank=False, null=False)

    def __str__(self):
        return(self.name)
    
class Document(models.Model):
    title = models.CharField(max_length=50)
    document = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title