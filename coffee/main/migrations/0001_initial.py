# Generated by Django 4.1.4 on 2022-12-22 16:40

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
                ('id', models.SmallAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='название')),
                ('is_published', models.BooleanField(default=True, verbose_name='публикация')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.SmallAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('mon', 'понедельник'), ('tue', 'вторник'), ('wen', 'среда'), ('thu', 'четверг'), ('fri', 'пятница'), ('sat', 'суббота'), ('sun', 'воскресение')], max_length=15, unique=True, verbose_name='день недели')),
                ('opening_time', models.TimeField(blank=True, null=True, verbose_name='время открытия')),
                ('closing_time', models.TimeField(blank=True, null=True, verbose_name='время закрытия')),
            ],
            options={
                'verbose_name': 'график работы',
                'verbose_name_plural': 'график работы',
                'db_table': 'main_work_schedule',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.SmallAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
                ('descr', models.CharField(max_length=2048, verbose_name='описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='публикация')),
                ('image', models.ImageField(upload_to='products/', verbose_name='картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'db_table': 'main_products',
            },
        ),
    ]
