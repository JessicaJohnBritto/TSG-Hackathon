# Generated by Django 2.2.9 on 2021-11-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, null=True)),
                ('fullname', models.CharField(max_length=250, null=True)),
                ('rollno', models.CharField(max_length=10, null=True)),
                ('role', models.CharField(choices=[('Admin', 'ADMIN'), ('Tsg Official', 'TSG OFFICIAL'), ('Governer', 'GOVERNER'), ('Student', 'STUDENT')], default='Student', max_length=30)),
                ('societies', models.ManyToManyField(blank=True, to='TSGhackathon.Society')),
            ],
        ),
    ]