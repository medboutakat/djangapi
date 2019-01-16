from django.db import models

# Create your models here.
class test(models.Model):
    name1 = models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)
    name3 = models.CharField(max_length=30)
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    def __str__(self):
        return self.name1