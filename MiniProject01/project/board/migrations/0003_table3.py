# Generated by Django 2.2.5 on 2020-01-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_table4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table3',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('writer', models.CharField(max_length=50)),
            ],
        ),
    ]
