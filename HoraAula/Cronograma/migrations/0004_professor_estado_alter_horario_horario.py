# Generated by Django 4.1.7 on 2023-05-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cronograma', '0003_alter_professor_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='estado',
            field=models.CharField(default=2, help_text='Sigla do estado', max_length=2, verbose_name='Estado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario',
            field=models.CharField(help_text='Horario da disciplina', max_length=20, verbose_name='horario'),
        ),
    ]