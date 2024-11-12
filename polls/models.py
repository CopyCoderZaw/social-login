from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

##### CustomUser
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, unique=True,null=True)
    email = models.EmailField(max_length=59,null=True,unique=True)
    profile = models.ImageField(default='pro.jpg', upload_to='image/')
    
### city weather
class City(models.Model):
    name = models.CharField(max_length=25, null=True,blank=True)
    
    def __str__ (self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'cities'
        
#### year date
class Year(models.Model):
    name = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.name
    
#### arakan photo
class Photo(models.Model):
    year = models.ForeignKey( Year, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 50, null=True)
    image = models.ImageField(upload_to='arakanimg/', null=True)
    
    def __str__(self):
        return self.title