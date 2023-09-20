# Generated by Django 4.2.4 on 2023-09-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='turno',
            name='horario',
            field=models.CharField(choices=[('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00')], max_length=20),
        ),
        migrations.AlterField(
            model_name='turno',
            name='motivo',
            field=models.CharField(choices=[('Asesoramiento integral.', 'Asesoramiento integral.'), ('Gestión de documentos argentinos.', 'Gestión de documentos argentinos.'), ('Gestión de documentos italianos.', 'Gestión de documentos italianos.'), ('Juicio por falta de turnos.', 'Juicio por falta de turnos.'), ('Asesoramiento por ciudadanías en Italia.', 'Asesoramiento por ciudadanías en Italia.'), ('Asesoramiento por ciudadanías via consulado italiano.', 'Asesoramiento por ciudadanías via consulado italiano.')], max_length=100),
        ),
        migrations.AlterField(
            model_name='turno',
            name='profesional',
            field=models.CharField(choices=[('Dr. Nicolas Vaca Cianferoni', 'Dr. Nicolas Vaca Cianferoni'), ('Dra. Agustina Afur', 'Dra. Agustina Afur')], max_length=50),
        ),
    ]