from django.db import models

# Create your models here.
from django.db import models

#About Info
class AboutInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()

#Contact Request
class ContactRequest (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=250, default='Default Subject')
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"message from {self.name} on {self.subject}"
    

#Testimonials
class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, blank=True)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date = models.DateField()
    
    def __str__(self):
        return f"Testimonial by {self.name}"
        