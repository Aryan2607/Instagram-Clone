# Generated by Django 3.1.8 on 2022-06-23 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20220623_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='Email',
        ),
    ]
