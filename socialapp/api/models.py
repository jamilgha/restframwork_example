from django.db import models

# Create your models here.

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])
class user (models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,help_text="clint User Name",unique=True)
    emailaddress=models.EmailField(max_length=300,help_text="clinte Email Address")
    name=models.CharField(max_length=300,help_text="Name")
    mobile=models.CharField(max_length=11)
    password=models.CharField(max_length=50)
    lastlogin=models.DateTimeField()
    locations=models.CharField(max_length=60)
    profileimage=models.ImageField(blank=True,upload_to='userprofile')
    family=models.CharField(max_length=300,help_text="clint family name")
    createdOn=models.DateTimeField()
    updateOn=models.DateTimeField(default=None)
    borndate=models.DateField()

    def __str__(self):
        return self.username
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    media_surce=models.ImageField(blank=True,upload_to='post_surce')
    user_post=models.ForeignKey(user,models.CASCADE,to_field='username')
    def __str__(self):
        return [self.user_post,"     ",self.media_surce]
