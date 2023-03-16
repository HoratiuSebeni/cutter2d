# Generated by Django 4.1.7 on 2023-03-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_alter_board_author_alter_edge_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockboard',
            options={'ordering': ['id', 'companyName', 'idBoard']},
        ),
        migrations.AlterModelOptions(
            name='stockedge',
            options={'ordering': ['id', 'companyName', 'idEdge']},
        ),
        migrations.AlterField(
            model_name='stockboard',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stockedge',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]