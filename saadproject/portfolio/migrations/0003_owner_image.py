# Generated by Django 4.2.13 on 2024-07-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='image',
            field=models.ImageField(default='', upload_to='owner_images/'),
            preserve_default=False,
        ),
    ]
