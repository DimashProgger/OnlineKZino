# Generated by Django 2.2.7 on 2019-12-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0012_ptslides'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouletteSlides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('slide', models.ImageField(upload_to='RouletteSlides')),
            ],
        ),
    ]