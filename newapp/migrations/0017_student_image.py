# Generated by Django 3.1.8 on 2022-06-29 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0016_auto_20220627_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Image',
            field=models.ImageField(null=b'I01\n', upload_to=''),
            preserve_default=b'I01\n',
        ),
    ]