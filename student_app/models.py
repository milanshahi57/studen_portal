from django.db import models

# Create your models here.
class Subject(models.Model):
    YEAR_CHOICES = [
        ('first', 'First Year'),
        ('second', 'Second Year'),
        ('third', 'Third Year'),
        ('fourth', 'Fourth Year'),
    ]
    
    name = models.CharField(max_length=200)  # Name of the subject
    year = models.CharField(choices=YEAR_CHOICES, max_length=10)  # Year for the subject
    image = models.ImageField(upload_to='subjects/', blank=True, null=True)  # Subject image


    
    def __str__(self):
        return self.name

