# Generated by Django 3.1 on 2020-08-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200825_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usrCreationDate',
            field=models.DateTimeField(),
        ),
    ]