from django.db import models

class WishlistItem(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()
    loja = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('em_analise', 'Em Análise'),
            ('comprado', 'Comprado')
        ],
        default='pendente'
    )
    data_adicao = models.DateTimeField(auto_now_add=True)
    ordem_personalizada = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordem_personalizada', 'nome']

    def __str__(self):
        return self.nome

    def to_markdown(self):
        return f"- {'[x]' if self.status == 'comprado' else '[ ]'} {self.nome}\n  - Preço: R$ {self.preco}\n  - Link: {self.link}"