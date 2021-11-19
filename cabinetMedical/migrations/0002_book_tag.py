# Generated by Django 3.2.9 on 2021-11-14 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinetMedical', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('statu', models.CharField(choices=[('comidy', 'comidy'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror')], max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('ville', models.CharField(max_length=100, null=True)),
                ('projet1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinetMedical.projet1')),
                ('tags', models.ManyToManyField(to='cabinetMedical.Tag')),
            ],
        ),
    ]