class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print (id(p))
    
    print(p.nome)
    p = Pessoa('Alexandre')
    print(p.nome)
    
    print (id(p))
    print(p.cumprimentar())  # Maneira mais usada
    print(Pessoa.cumprimentar(p))
    p.nome = 'Elaine'
    print(p.nome)
