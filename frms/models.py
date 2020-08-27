from django.db import models
from user import models as M

# Create your models here.
class Forms(models.Model):
    usrID=models.ForeignKey(M.user,on_delete=models.CASCADE)
    frmID=models.IntegerField(default=1,primary_key=True)
    frmName=models.CharField(max_length=20)
    frmTitle=models.CharField(max_length=20)
    frmCreatedOn=models.DateTimeField()
    frmStatus=models.CharField(max_length=20)
    frmGroup=models.CharField(max_length=20)
    frmPublishDate=models.DateField()
    frmEndDate=models.DateField()
    frmURL=models.CharField(max_length=50)
    frmDescription=models.CharField(max_length=100)