# Generated by Django 3.2.9 on 2021-11-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesticide', '0003_pesticide_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesticide',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]