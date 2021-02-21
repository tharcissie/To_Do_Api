from django.db import models

# Create your models here.
class ToDo(models.Model):

    PRIORITY = (
        ('LOW','LOW'),
        ('MEDIUM','MEDIUM'),
        ('HIGH','HIGH')
    )

    title         = models.CharField(max_length=300)
    description   = models.TextField()
    priority      = models.CharField(max_length=10,choices=PRIORITY, default='Active')
    created_date  = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


