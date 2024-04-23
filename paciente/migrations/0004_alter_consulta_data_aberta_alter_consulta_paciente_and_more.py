# Generated by Django 5.0.4 on 2024-04-23 19:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0006_alter_dadosmedico_especialidade_and_more'),
        ('paciente', '0003_alter_consulta_data_aberta_alter_consulta_paciente_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data_aberta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medico.datasabertas'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documento',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paciente.consulta'),
        ),
    ]
