# Generated by Django 3.2.8 on 2021-10-07 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20211007_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='times',
            name='gym',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time', to='main_app.gyms'),
        ),
    ]
