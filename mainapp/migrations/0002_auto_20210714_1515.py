# Generated by Django 3.2.5 on 2021-07-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
    ]
