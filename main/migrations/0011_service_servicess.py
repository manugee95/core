# Generated by Django 4.1.4 on 2022-12-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_service_columbia_alter_service_maryland_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='servicess',
            field=models.BooleanField(default=True),
        ),
    ]
