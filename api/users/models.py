from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=255, null=False, blank=False)
    document = models.CharField(verbose_name='CPF', max_length=11, null=False, blank=False)
    email = models.EmailField(verbose_name='E-mail', null=False, blank=False)
    telephone = models.CharField(verbose_name='Telefone', max_length=11, null=False, blank=False)
    birth_date = models.DateField(verbose_name='Nascimento', null=False, blank=False)
    street = models.CharField(verbose_name='Rua', max_length=255, null=False, blank=False)
    district = models.CharField(verbose_name='Bairro', max_length=255, null=False, blank=False)
    city = models.CharField(verbose_name='Cidade', max_length=255, null=False, blank=False)

    STATES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )

    state = models.CharField(verbose_name='Estado', max_length=2, choices=STATES, null=False, blank=False)
    comments = models.CharField(verbose_name='Observações', max_length=255, blank=True)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return str(self.name)
