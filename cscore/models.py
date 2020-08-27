from django.db import models
from user import models as M
# Create your models here.
class cscore(models.Model):
    csxID=models.IntegerField(primary_key=True)
    csxName=models.CharField(max_length=50)
    csxDescription=models.CharField(max_length=100)
    csxCreatedOn=models.DateTimeField()
    usrID=models.ForeignKey(M.user,on_delete=models.CASCADE)
    csxStatus=models.CharField(max_length=20)