# Generated by Django 4.2.5 on 2023-09-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CondicoesVeiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condicao', models.CharField(max_length=25)),
                ('ano', models.PositiveSmallIntegerField()),
                ('cor', models.CharField(max_length=50)),
                ('quilometragem', models.IntegerField()),
                ('leilao', models.BooleanField()),
            ],
            options={
                'db_table': 'condicoes_veiculos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'marcas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modelos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'modelos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Veiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagamento', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'veiculos',
                'managed': False,
            },
        ),
    ]
