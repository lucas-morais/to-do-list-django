# Generated by Django 4.0.6 on 2022-08-07 11:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('finished', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('L', 'Leisure'), ('W', 'Work')], max_length=1)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]