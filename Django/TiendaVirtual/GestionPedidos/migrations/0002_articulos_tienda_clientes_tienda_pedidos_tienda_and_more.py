# Generated by Django 4.0.6 on 2022-07-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos_Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Seccion', models.CharField(max_length=30)),
                ('Precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes_Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Direccion', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos_Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('Entregado', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Articulos',
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.DeleteModel(
            name='Pedidos',
        ),
    ]