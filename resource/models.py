from django.db import models

# Create your models here.
class Post(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     catagory= models.CharField(max_length=100)
     area= models.CharField(max_length=255)
     details= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
         return "Message from"+ self.name +'-'+self.email