# Generated by Django 3.2.6 on 2021-08-11 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_auth', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profiles')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account_auth.siteuser')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
        ),
    ]
