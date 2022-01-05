# Generated by Django 2.2.9 on 2021-12-21 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TSGhackathon', '0003_remove_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Technology', 'Technology'), ('Social-Culture', 'Social-Culture'), ('Sports-Games', 'Sports-Games'), ('Student Welfare', 'Student-Welfare'), ('Others', 'Others')], default='Technology', max_length=30)),
                ('photo', models.FileField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=250, null=True)),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TSGhackathon.Profile')),
            ],
        ),
    ]