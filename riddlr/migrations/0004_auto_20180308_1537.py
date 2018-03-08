# Generated by Django 2.0.3 on 2018-03-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddlr', '0003_auto_20180308_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riddle',
            name='author',
        ),
        migrations.AlterField(
            model_name='riddle',
            name='date_posted',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='riddle',
            name='difficulty',
            field=models.IntegerField(default=75),
        ),
        migrations.AlterField(
            model_name='riddle',
            name='num_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='riddle',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
