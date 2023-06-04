# Generated by Django 3.2.15 on 2023-06-04 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категорія')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='doctors',
            options={'ordering': ['id'], 'verbose_name': 'Лікарі', 'verbose_name_plural': 'Лікарі'},
        ),
        migrations.AddField(
            model_name='doctors',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='doctors.category', verbose_name='Категорії'),
        ),
    ]
