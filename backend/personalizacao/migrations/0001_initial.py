# Generated by Django 4.2.6 on 2023-11-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('imagem_banner', models.ImageField(upload_to='banners/')),
                ('ativa', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'promocoes',
                'managed': False,
            },
        ),
    ]
