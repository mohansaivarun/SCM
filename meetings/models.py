from django.db import models
from user import models as M
# Create your models here.
class meetings(models.Model):
    mtgID=models.IntegerField(primary_key=True)
    usrID=models.ForeignKey(M.user,on_delete=models.CASCADE)
    mtgTitle=models.CharField(max_length=50)
    mtgDescription=models.CharField(max_length=100)
    mtgDate=models.DateField()
    mtgAttendees=models.CharField(max_length=500)
    mtgTime=models.TimeField()
    mtgType=models.CharField(max_length=20)
    mtgAgenda=models.CharField(max_length=50)
    mtgRemarks=models.CharField(max_length=50)
    mtgReminderFreq=models.TimeField()
    mtgLocation=models.CharField(max_length=20)
    