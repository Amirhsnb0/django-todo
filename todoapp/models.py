from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class todoItem (models.Model):
    work= models.CharField(max_length=250)
    check = models.BooleanField(default=False)
    date =models.DateTimeField(null=True , blank=True)
    owner= models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def check_item(self):
        self.check =True
        
    def __str__(self) :
        return self.work
