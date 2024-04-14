from django.db import models

# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    create_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True)
    
    
    