# Generated by Django 4.0.5 on 2022-07-01 12:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_comentario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-created'], 'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterField(
            model_name='comentario',
            name='coment',
            field=ckeditor.fields.RichTextField(verbose_name='Comentario'),
        ),
    ]
