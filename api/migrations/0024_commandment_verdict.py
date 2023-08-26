# Generated by Django 4.0 on 2023-08-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commandment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Заповедь',
                'verbose_name_plural': 'Заповеди',
                'db_table': 'commandments',
            },
        ),
        migrations.CreateModel(
            name='Verdict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Вердикт',
                'verbose_name_plural': 'Вердикты',
                'db_table': 'verdicts',
            },
        ),
    ]
