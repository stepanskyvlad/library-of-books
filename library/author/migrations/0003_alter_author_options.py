# Generated by Django 4.1 on 2023-02-16 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_author_books_author_name_author_patronymic_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['id']},
        ),
    ]
