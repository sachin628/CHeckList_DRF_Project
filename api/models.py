from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class CheckList(models.Model):
    title = models.CharField(max_length=260)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CheckListItem(models.Model):
    text = models.CharField(max_length=300)
    is_checked =models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    Checklist = models.ForeignKey(CheckList,on_delete=models.CASCADE)
    user =models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
