from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('link', models.URLField()),
                ('loja', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('em_analise', 'Em Análise'), ('comprado', 'Comprado')], default='pendente', max_length=20)),
                ('data_adicao', models.DateTimeField(auto_now_add=True)),
                ('ordem_personalizada', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['ordem_personalizada', 'nome'],
            },
        ),
    ]