# Generated by Django 4.2.7 on 2023-12-12 03:16

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ruc', models.CharField(max_length=13, unique=True)),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Empresa')),
                ('direccion', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ('nombre',),
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vacante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
                ('carreraRequerida', models.CharField(choices=[('SOF', 'Ingeniería en Software'), ('BIO', 'Biotecnología'), ('IND', 'Ingeniería Industrial'), ('AMB', 'Ingeniería Ambiental'), ('ALI', 'Ingeniería de Alimentos'), ('MUL', 'Producción Audiovisual'), ('ADM', 'Administración de Empresas'), ('CON', 'Contabilidad y Auditoría'), ('TUR', 'Turismo'), ('COM', 'Comunicación'), ('ECO', 'Economía'), ('ENF', 'Enfermería'), ('NUT', 'Nutrición y Dietética'), ('FIS', 'Fisioterapia'), ('MED', 'Medicina'), ('PAD', 'Pedagogía de la Actividad Física y Deporte'), ('EDU', 'Educación'), ('PED', 'Pedagogía de los Idiomas Nacionales y Extranjeros'), ('EES', 'Educación Especial'), ('PLL', 'Pedagogía de la Lengua y Literatura')], max_length=3)),
                ('nivelRequerido', models.CharField(choices=[('BAC', 'Bachiller'), ('TER', 'Tercer Nivel'), ('POS', 'Posgrado')], max_length=3)),
                ('ubicacion', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaIni', models.DateField()),
                ('fechaFin', models.DateField()),
                ('cupos', models.PositiveSmallIntegerField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa')),
            ],
        ),
    ]
