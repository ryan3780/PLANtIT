# Generated by Django 3.2.9 on 2021-12-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(default='안녕하세요~ 잘 부탁드립니다! ~ヾ(＾∇＾)', max_length=256, null=True),
        ),
    ]