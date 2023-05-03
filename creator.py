from faker import Faker

faker = Faker('pt_BR')

import random

def generate_rg():
    rg = ""
    for i in range(9):
        rg += str(random.randint(0, 9))
    return rg
def generate_cpf():
    cpf = [random.randint(0, 9) for i in range(9)]
    cpf.extend(random.randint(0, 2) for i in range(2))
    return "".join(map(str, cpf))

for i in range(100):
    email = faker.email()
    cpf = generate_cpf()
    rg = generate_rg()
    nome_completo = faker.name()
    senha = faker.password(length=15, special_chars=False, upper_case=False)
    data_nascimento = faker.date_of_birth().strftime('%d-%m-%Y')
    status = random.choice(['A', 'I'])
    nome_social = faker.name() if random.choice([True, False]) else ''

    print(f"INSERT INTO T_CLIENTE (nm_email, nr_cpf, nr_rg, nm_cliente, nm_senha, dt_nascimento, st_cliente, nm_social) VALUES ('{email}', '{cpf}', '{rg}', '{nome_completo}', '{senha}', '{data_nascimento}', '{status}', '{nome_social}');")
