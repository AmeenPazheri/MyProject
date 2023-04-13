# Generated by Django 4.2 on 2023-04-09 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('dep_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=100)),
                ('dep_img', models.ImageField(upload_to='pics')),
                ('dep_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('hod_img', models.ImageField(upload_to='pics')),
                ('course_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.department')),
            ],
        ),
    ]