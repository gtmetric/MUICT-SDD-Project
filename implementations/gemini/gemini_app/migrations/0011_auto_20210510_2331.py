# Generated by Django 3.2 on 2021-05-10 16:31

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gemini_app', '0010_auto_20210510_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='scienceplan',
            name='status',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='color_type',
            field=models.CharField(choices=[('Color mode', 'Color mode'), ('B&W mode', 'B&W mode')], default='color_mode', max_length=255),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='end_date',
            field=models.DateTimeField(default='10/05/2021 16:31:12', validators=[django.core.validators.MinValueValidator(datetime.datetime(2021, 5, 10, 16, 31, 12, 251106, tzinfo=utc), message='The end date is invalid.')]),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='file_quality',
            field=models.CharField(choices=[('Low', 'Low'), ('Fine', 'Fine')], default='fine', max_length=255),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='file_type',
            field=models.CharField(choices=[('PNG', 'PNG'), ('JPEG', 'JPEG'), ('RAW', 'RAW')], default='png', max_length=255),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='star_system',
            field=models.CharField(choices=[('Andromeda', 'Andromeda'), ('Antlia', 'Antlia'), ('Apus', 'Apus'), ('Aquarius', 'Aquarius'), ('Aquila', 'Aquila'), ('Ara', 'Ara'), ('Aries', 'Aries'), ('Auriga', 'Auriga'), ('Boötes', 'Boötes'), ('Caelum', 'Caelum'), ('Camelopardalis', 'Camelopardalis'), ('Cancer', 'Cancer'), ('CanesVenatici', 'CanesVenatici'), ('CanisMajor', 'CanisMajor'), ('CanisMinor', 'CanisMinor'), ('Capricornus', 'Capricornus'), ('Carina', 'Carina'), ('Cassiopeia', 'Cassiopeia'), ('Centaurus', 'Centaurus'), ('Cepheus', 'Cepheus'), ('Cetus', 'Cetus'), ('Chamaeleon', 'Chamaeleon'), ('Circinus', 'Circinus'), ('Columba', 'Columba'), ('ComaBerenices', 'ComaBerenices'), ('CoronaAustralis', 'CoronaAustralis'), ('CoronaBorealis', 'CoronaBorealis'), ('Corvus', 'Corvus'), ('Crater', 'Crater'), ('Crux', 'Crux'), ('Cygnus', 'Cygnus'), ('Delphinus', 'Delphinus'), ('Dorado', 'Dorado'), ('Draco', 'Draco'), ('Equuleus', 'Equuleus'), ('Eridanus', 'Eridanus'), ('Fornax', 'Fornax'), ('Gemini', 'Gemini'), ('Grus', 'Grus'), ('Hercules', 'Hercules'), ('Horologium', 'Horologium'), ('Hydra', 'Hydra'), ('Hydrus', 'Hydrus'), ('Indus', 'Indus'), ('Lacerta', 'Lacerta'), ('Leo', 'Leo'), ('LeoMinor', 'LeoMinor'), ('Lepus', 'Lepus'), ('Libra', 'Libra'), ('Lupus', 'Lupus'), ('Lynx', 'Lynx'), ('Lyra', 'Lyra'), ('Mensa', 'Mensa'), ('Microscopium', 'Microscopium'), ('Monoceros', 'Monoceros'), ('Musca', 'Musca'), ('Norma', 'Norma'), ('Octans', 'Octans'), ('Ophiuchus', 'Ophiuchus'), ('Orion', 'Orion'), ('Pavo', 'Pavo'), ('Pegasus', 'Pegasus'), ('Perseus', 'Perseus'), ('Phoenix', 'Phoenix'), ('Pictor', 'Pictor'), ('Pisces', 'Pisces'), ('PiscisAustrinus', 'PiscisAustrinus'), ('Puppis', 'Puppis'), ('Pyxis', 'Pyxis'), ('Reticulum', 'Reticulum'), ('Sagitta', 'Sagitta'), ('Sagittarius', 'Sagittarius'), ('Scorpius', 'Scorpius'), ('Sculptor', 'Sculptor'), ('Scutum', 'Scutum'), ('Serpens', 'Serpens'), ('Sextans', 'Sextans'), ('Taurus', 'Taurus'), ('Telescopiu', 'Telescopiu'), ('Triangulum', 'Triangulum'), ('TriangulumAustrale', 'TriangulumAustrale'), ('Tucana', 'Tucana'), ('UrsaMajor', 'UrsaMajor'), ('UrsaMinor', 'UrsaMinor'), ('Vela', 'Vela'), ('Virgo', 'Virgo'), ('Volans', 'Volans'), ('Vulpecula', 'Vulpecula')], default='Andromeda', max_length=255),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='start_date',
            field=models.DateTimeField(default='10/05/2021 16:31:12', validators=[django.core.validators.MinValueValidator(datetime.datetime(2021, 5, 10, 16, 31, 12, 251106, tzinfo=utc), message='The start date is invalid.')]),
        ),
    ]
