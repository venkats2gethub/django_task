# Generated by Django 2.2 on 2019-08-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
                ('text3', models.TextField()),
                ('text4', models.IntegerField()),
                ('text5', models.TextField()),
                ('text6', models.TextField()),
                ('num1', models.IntegerField()),
                ('text7', models.TextField()),
                ('date1', models.DateField()),
                ('num2', models.FloatField()),
            ],
        ),
    ]