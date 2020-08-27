from django.db import models
from user import models as M

# Create your models here.
class Document(models.Model):
    usrID=models.ForeignKey(M.user,on_delete=models.CASCADE)
    docID=models.IntegerField(default=1,unique=True,primary_key=True)
    docTitle=models.CharField(max_length=20)
    docDescription=models.CharField(max_length=50)
    docLink=models.CharField(max_length=100)
    docCreatedon=models.DateTimeField()
    docStatus=models.CharField(max_length=20)
    docRemark=models.CharField(max_length=50)