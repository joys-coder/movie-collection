# Generated by Django 4.0.4 on 2022-05-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='img',
            field=models.ImageField(default='happy', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
