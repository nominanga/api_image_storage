# Generated by Django 4.2 on 2023-05-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='color',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]