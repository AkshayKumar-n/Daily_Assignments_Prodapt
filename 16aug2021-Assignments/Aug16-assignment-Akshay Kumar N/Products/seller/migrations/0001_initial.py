# Generated by Django 3.0.4 on 2021-08-17 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sellerid', models.IntegerField()),
                ('sellername', models.CharField(max_length=50)),
                ('selleraddress', models.CharField(max_length=50)),
                ('sellerphno', models.CharField(max_length=50)),
            ],
        ),
    ]
