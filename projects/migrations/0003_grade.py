# Generated by Django 3.2.4 on 2022-12-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradeId', models.CharField(max_length=100)),
                ('projectId', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
