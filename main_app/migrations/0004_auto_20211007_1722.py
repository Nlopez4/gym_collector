# Generated by Django 3.2.8 on 2021-10-07 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_classtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='times',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('time', models.IntegerField(default=0)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='main_app.gyms')),
            ],
        ),
        migrations.DeleteModel(
            name='classTime',
        ),
    ]
