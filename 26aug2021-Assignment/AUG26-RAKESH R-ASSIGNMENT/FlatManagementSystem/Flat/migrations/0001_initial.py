# Generated by Django 3.2.6 on 2021-08-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_no', models.CharField(max_length=100)),
                ('building_no', models.CharField(max_length=150)),
                ('owner_name', models.CharField(max_length=150)),
                ('mobile_no', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('aadhar_no', models.CharField(max_length=150)),
                ('email_id', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]
