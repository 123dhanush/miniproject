# Generated by Django 2.2b1 on 2019-03-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('n_duties', models.IntegerField()),
                ('n_am', models.IntegerField()),
                ('n_pm', models.IntegerField()),
                ('n_relief', models.IntegerField()),
                ('priority', models.IntegerField()),
            ],
        ),
    ]