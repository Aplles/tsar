# Generated by Django 4.0 on 2023-09-15 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('verdict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.verdict', verbose_name='Вердикт')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'db_table': 'books',
            },
        ),
    ]
