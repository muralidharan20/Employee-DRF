# Generated by Django 4.1.7 on 2023-03-21 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('salary', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(default=1)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
