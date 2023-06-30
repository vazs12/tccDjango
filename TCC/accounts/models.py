from django.db import models

# Create your models here.

class Student(models.Model):
    TURMAS = (
        ("turma_a", "Turma A"),
        ("turma_b", "Turma B"),
    )
    ESTADOS = (
        ("sp", "São Paulo"),
        ("mg", "Minas Gerais"),
        ("ac", "Acre"),
        ("al", "Alagoas"),
        ("ap", "Amapá"),
        ("am", "Amazonas"),
        ("ba", "Bahia"),
        ("ce", "Ceará"),
        ("df", "Distrito Federal"),
        ("es", "Espírito Santo"),
        ("go", "Goiás"),
        ("ma", "Maranhão"),
        ("mt", "Mato Grosso"),
        ("ms", "Mato Grosso do Sul"),
        ("pa", "Pará"),
        ("pb", "Paraíba"),
        ("pr", "Paraná"),
        ("pe", "Pernambuco"),
        ("pi", "Piauí"),
        ("rj", "Rio de Janeiro"),
        ("rn", "Rio Grande do Norte"),
        ("rs", "Rio Grande do Sul"),
        ("ro", "Rondônia"),
        ("rr", "Roraima"),
        ("sc", "Santa Catarina"),
        ("se", "Sergipe"),
        ("to", "Tocantins"),
    )
    nome_aluno = models.CharField(max_length=100)
    cpf_aluno = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=ESTADOS[0][0])
    cep = models.CharField(max_length=8)
    turma = models.CharField(max_length=10, choices=TURMAS, default=TURMAS[0][0])


    def __str__(self):
        return f"{self.nome_aluno} - {self.cpf_aluno}"