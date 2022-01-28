# Generated by Django 4.0 on 2022-01-28 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('use', models.TextField(blank=True)),
                ('diametr', models.FloatField(blank=True)),
                ('len', models.IntegerField(blank=True)),
                ('color', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.category')),
            ],
        ),
    ]