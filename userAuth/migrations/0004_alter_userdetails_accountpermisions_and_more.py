# Generated by Django 4.1.7 on 2023-02-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0003_rename_amount_stock_nopieces_board_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='accountPermisions',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='accountType',
            field=models.CharField(max_length=20),
        ),
    ]