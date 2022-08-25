from utils.helper import formata_float_str_moeda

class Produto:
    contador: int = 1

    def __init__(self, nome, preco):
        self.codigo = Produto.contador
        self.nome = nome
        self.preco = preco
        Produto.contador += 1

    def __str__(self) -> str:
       return f'Código: {self.codigo} \nNome: {self.nome} \nPreço: {formata_float_str_moeda(self.preco)}'

