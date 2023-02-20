# Generated by Django 4.1.7 on 2023-02-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('appointment_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('department_id', models.IntegerField(null=True, verbose_name=3)),
                ('created_by', models.IntegerField(null=True, verbose_name=3)),
                ('deleted_by', models.IntegerField(null=True, verbose_name=3)),
            ],
        ),
    ]
