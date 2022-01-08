import random
import PySimpleGUI as sg
class SimuladorDeDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.messagem = "Gostaria de Rolar um dado?"
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado')],
            [sg.Button('sim'),sg.Button('nao')]
        ]


    def iniciar(self):
        # Criar uma Janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com valores
        try:
            if  self.eventos == 'sim'or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'nao' or self.eventos  == 'n':
                print("Obrigado Por ultilizar o dado")
            else:
                print("Insira Sim ou Nao")
        except:
            print("Erro na entrada de dados")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
simulador = SimuladorDeDados()
simulador.iniciar()