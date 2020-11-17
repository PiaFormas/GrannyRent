# Generated by Django 3.1.3 on 2020-11-17 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjeta',
            name='comprador',
        ),
        migrations.AddField(
            model_name='comprador',
            name='usuario_comprador',
            field=models.CharField(default='a', help_text='Usuario Comprador', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendedor',
            name='usuario_vendedor',
            field=models.CharField(default='a', help_text='Usuario Vendedor', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comprador',
            name='apellido_comprador',
            field=models.CharField(help_text='Apellido Comprador', max_length=15),
        ),
        migrations.AlterField(
            model_name='comprador',
            name='nombre_comprador',
            field=models.CharField(help_text='Nombre Comprador', max_length=15),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='apellido_vendedor',
            field=models.CharField(help_text='Apellido Vendedor', max_length=30),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='nombre_vendedor',
            field=models.CharField(help_text='Nombre Vendedor', max_length=30),
        ),
        migrations.DeleteModel(
            name='CuentaBanco',
        ),
        migrations.DeleteModel(
            name='Tarjeta',
        ),
    ]