from tkinter import *
import requests

janela = Tk()

class Functions():
   def gerar(self):

       cep_input = self.en_pesquisar.get()
       request = requests.get( 'https://viacep.com.br/ws/{}/json/'.format( cep_input ) )

       address_data = request.json()
       if 'erro' not in address_data:
           self.lbl_cep['text']   = cep_input
           self.lbl_lugar['text'] = address_data['localidade'] + '/' + address_data['uf']


class Janela(Functions):
    def __init__(self):

        self.janela = janela
        self.configuracoes()
        self.widgets()

        janela.mainloop()

    def configuracoes(self):
        janela.geometry("480x200")
        self.janela.resizable(False,False)
        janela.title('Consultar CEP')

    def widgets(self):
        #Apresentacao
        self.frame = Frame(self.janela, bg='#38385c')
        self.frame.place(relheight=0.25, relwidth=1)

        self.frame_result = Frame( self.janela, bg='#e6e6e6' )
        self.frame_result.place( rely=0.25, relheight=0.8, relwidth=1 )

        self.en_pesquisar = Entry( self.frame)
        self.en_pesquisar.place(relx= 0.1, rely= 0.3,relheight=0.5, relwidth=0.5 )

        self.botao = Button( self.frame, text='Pesquisar', command = self.gerar)
        self.botao.place(relx= 0.63, rely= 0.3, relheight=0.5, relwidth=0.25)

        self.lbl = Label(self.frame_result, text = 'Localidade/UF', bg='#999999')
        self.lbl.place(relx= 0.02, rely=0.12, relheight = 0.18, relwidth = 0.45)


        self.lbl2 = Label(self.frame_result, text = 'CEP', bg='#999999')
        self.lbl2.place(relx= 0.53, rely=0.12, relheight = 0.18, relwidth = 0.45)

        self.lbl_lugar = Label( self.frame_result, bg ='#bfbfbf')
        self.lbl_lugar.place( relx=0.02, rely=0.32, relheight=0.18, relwidth=0.45 )

        self.lbl_cep = Label( self.frame_result, bg ='#bfbfbf')
        self.lbl_cep.place( relx=0.53, rely=0.32, relheight=0.18, relwidth=0.45 )


Janela()