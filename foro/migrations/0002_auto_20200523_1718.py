# Generated by Django 3.0.6 on 2020-05-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foro',
            name='foto_foro',
            field=models.ImageField(default='forum_pics', upload_to=''),
        ),
    ]
