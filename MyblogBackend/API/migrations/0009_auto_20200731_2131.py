# Generated by Django 2.2.13 on 2020-07-31 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_auto_20200731_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='discuss_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.User'),
        ),
    ]
