# Generated by Django 5.0 on 2024-10-20 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='arakanimg/')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.year')),
            ],
        ),
    ]
