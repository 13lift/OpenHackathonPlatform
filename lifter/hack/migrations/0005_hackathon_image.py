# Generated by Django 2.0.13 on 2019-04-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0004_auto_20190408_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
