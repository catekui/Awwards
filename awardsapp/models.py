from django.db import models
from django.contrib.auth.models import User


# Create your models here.



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  
    bio = models.TextField(max_length=400, blank=True,null=True)
    email = models.CharField(max_length=400, null=True, blank=True)
    project = models.CharField

    
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.save()
        
    def update(self):
        self.save()
    
    def __str__(self):
        return f'{self.user.username} Profile'


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     date_created = models.DateTimeField(auto_now_add=True)

# class Project(models.Model):
#     # user = models.ForeignKey(User)
#     title = models.CharField(max_length=400)
#     image = models.ImageField(max_length=500)
#     description = models.TextField
#     link = models.URLField(max_length=1000)

#     def __str__(self):
#         return f'{self.user.username} Project'


# class Ratings(models.Model):
#     project_id = models.ForeignKey()
#     rating = models.IntegerField

#     def __str__(self):
#         return f'{self.user.username} Ratings'


