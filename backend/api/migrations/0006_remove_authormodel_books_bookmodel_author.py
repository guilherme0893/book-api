# Generated by Django 4.1.7 on 2023-03-14 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_authormodel_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authormodel',
            name='books',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.authormodel'),
        ),
    ]
