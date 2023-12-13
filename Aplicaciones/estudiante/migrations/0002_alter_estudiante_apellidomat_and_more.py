# Generated by Django 4.2.7 on 2023-12-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='apellidoMat',
            field=models.CharField(max_length=50, null=True, verbose_name='Apellido materno'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='apellidoPat',
            field=models.CharField(max_length=50, null=True, verbose_name='Apellido paterno'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='carrera',
            field=models.CharField(choices=[('SOF', 'Ingeniería en Software'), ('BIO', 'Biotecnología'), ('IND', 'Ingeniería Industrial'), ('AMB', 'Ingeniería Ambiental'), ('ALI', 'Ingeniería de Alimentos'), ('MUL', 'Producción Audiovisual'), ('ADM', 'Administración de Empresas'), ('CON', 'Contabilidad y Auditoría'), ('TUR', 'Turismo'), ('COM', 'Comunicación'), ('ECO', 'Economía'), ('ENF', 'Enfermería'), ('NUT', 'Nutrición y Dietética'), ('FIS', 'Fisioterapia'), ('MED', 'Medicina'), ('PAD', 'Pedagogía de la Actividad Física y Deporte'), ('EDU', 'Educación'), ('PED', 'Pedagogía de los Idiomas Nacionales y Extranjeros'), ('EES', 'Educación Especial'), ('PLL', 'Pedagogía de la Lengua y Literatura')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='cedula',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nivelEducativo',
            field=models.CharField(choices=[('BAC', 'Bachiller'), ('TER', 'Tercer Nivel'), ('POS', 'Posgrado')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]