# Generated by Django 2.2.5 on 2021-02-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210216_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_img',
            field=models.ImageField(blank=True, upload_to='group_image/'),
        ),
    ]
