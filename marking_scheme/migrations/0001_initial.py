# Generated by Django 5.1.1 on 2024-09-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarkingScheme',
            fields=[
                ('markingscheme_id', models.AutoField(primary_key=True, serialize=False)),
                ('module_id', models.IntegerField()),
                ('module_name', models.CharField(default=1, max_length=30)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
