# Generated by Django 2.2.6 on 2019-11-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0007_auto_20191107_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_banned',
            field=models.BooleanField(default=False),
        ),
    ]