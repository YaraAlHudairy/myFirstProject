from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=30)
    job = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Students'
        ordering = ('-name',)

