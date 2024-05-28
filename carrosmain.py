class ParteCarro:
    def __init__(self, nome):
        self.nome = nome
        self.subpartes = []

    def adicionar_subparte(self, subparte):
        self.subpartes.append(subparte)

    def remover_subparte(self, subparte):
        self.subpartes.remove(subparte)

    def mover_subparte(self, subparte, nova_posicao):
        if subparte in self.subpartes:
            self.subpartes.remove(subparte)
            self.subpartes.insert(nova_posicao, subparte)
        else:
            print(f"{subparte.nome} não encontrado")

    def __str__(self):
        return f"{self.nome}"

# Exemplo de uso
carro = ParteCarro("Carro")
motor = ParteCarro("Motor")
rodas = ParteCarro("Rodas")
assentos = ParteCarro("Assentos")

carro.adicionar_subparte(motor)
carro.adicionar_subparte(rodas)
carro.adicionar_subparte(assentos)

print("Carro e suas partes:")
for parte in carro.subpartes:
    print(parte)

# Movendo as partes
carro.mover_subparte(motor, 2)
print("\nCarro após mover o motor para a última posição:")
for parte in carro.subpartes:
    print(parte)

# Removendo uma parte
carro.remover_subparte(assentos)
print("\nCarro após remover os assentos:")
for parte in carro.subpartes:
    print(parte)
