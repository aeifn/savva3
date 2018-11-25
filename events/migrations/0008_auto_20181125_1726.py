# Generated by Django 2.1.2 on 2018-11-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20181117_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(blank=True, max_length=200, verbose_name='Предположительная тема')),
                ('date', models.DateTimeField(blank=True, verbose_name='Предлагаемая дата')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('name', models.CharField(max_length=40, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=200, verbose_name='Ваша электропочта')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
            ],
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start']},
        ),
    ]
