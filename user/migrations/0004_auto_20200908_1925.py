# Generated by Django 3.1 on 2020-09-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200825_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usrCity',
            field=models.CharField(default='Delhi', max_length=25),
        ),
        migrations.AddField(
            model_name='user',
            name='usrGender',
            field=models.CharField(default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='usrPhone',
            field=models.CharField(max_length=15),
        ),
    ]
