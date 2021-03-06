# Generated by Django 4.0.3 on 2022-03-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teeth_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('detected_image', models.ImageField(upload_to='imagesresult/')),
                ('teeth_score', models.TextField()),
            ],
        ),
    ]
