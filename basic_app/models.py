from django.db import models


class Services(models.Model):
    icon = models.TextField()  # For uploading icons/images
    heading = models.CharField(max_length=100)
    paragraph = models.TextField()

    def __str__(self):
        return self.heading


class course(models.Model):
    heading=models.CharField(max_length=100)
    paragraph= models.CharField(max_length=300)

    def __str__(self):
        return self.heading
    
class Get_In_Touch(models.Model):
    location=models.CharField(max_length=300)
    email=models.EmailField()
    phone=models.CharField(max_length=15)

    def __str__(self):
        return self.location



class ai_showcase(models.Model):
    ai_images=models.ImageField(upload_to='images/')
    ai_name=models.CharField(max_length=300)
    ai_name_details=models.CharField(max_length=250)
        
    def __str__(self):
        return self.ai_name
