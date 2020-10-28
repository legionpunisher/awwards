from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE )
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models. TextField()
    projects = models.ForeignKey(Project, on_delete=models.CASCADE,null = True,blank=True)
    contact = models.TextField()

    def __str__(self):
        return self.name.username

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls,identity):
        profile = Profile.objects.filter(name__username__icontains = identity)
        return profile

