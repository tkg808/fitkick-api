# Generated by Django 4.0.3 on 2022-04-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('exercise_type', models.CharField(choices=[('Aerobic', 'Aerobic'), ('Anaerobic', 'Anaerobic'), ('Mobility', 'Mobility')], default='', max_length=10)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('exercises', models.ManyToManyField(blank=True, related_name='workouts', to='fitkick.exercise')),
            ],
        ),
    ]
