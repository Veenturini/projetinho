# Generated by Django 4.0.5 on 2022-09-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_autor_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(related_name='livros', to='core.autor'),
        ),
    ]
