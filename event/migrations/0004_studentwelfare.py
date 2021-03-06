# Generated by Django 3.2.9 on 2021-11-30 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20211130_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentWelfare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('small_description', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='technology/')),
                ('description', models.TextField(null=True)),
                ('month_of_event', models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default='Jan', max_length=30)),
                ('date', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('type_of_event', models.CharField(choices=[('soon', 'soon'), ('att', 'att'), ('imp', 'imp')], default='soon', max_length=30)),
                ('day_of_event', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=30)),
                ('deadline', models.DateTimeField(auto_now_add=True, null=True)),
                ('SuperviserName', models.CharField(max_length=50, null=True)),
                ('SuperviserEmail', models.CharField(max_length=60, null=True)),
                ('SuperviserContact', models.CharField(max_length=30, null=True)),
                ('VenueName', models.CharField(max_length=60, null=True)),
                ('facebook', models.CharField(max_length=200, null=True)),
                ('linkedin', models.CharField(max_length=200, null=True)),
                ('instagram', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
