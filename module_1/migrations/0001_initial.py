# Generated by Django 5.1 on 2024-08-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_data_base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('empid', models.IntegerField()),
                ('department', models.CharField(max_length=250)),
                ('salary', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
