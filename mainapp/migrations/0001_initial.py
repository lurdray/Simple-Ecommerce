# Generated by Django 2.2.4 on 2020-03-20 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15)),
                ('image', models.ImageField(upload_to='images/')),
                ('descrp', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(default='', max_length=15)),
                ('name_owner', models.CharField(default='', max_length=35)),
                ('phone_owner', models.CharField(default='', max_length=15)),
                ('email_owner', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
            ],
        ),
    ]
