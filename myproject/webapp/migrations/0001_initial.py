# Generated by Django 2.0.4 on 2019-07-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=12)),
                ('lastname', models.CharField(max_length=12)),
                ('emp_id', models.IntegerField()),
            ],
        ),
    ]
