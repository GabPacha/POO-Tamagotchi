class Pessoa:
    def __init__(self,nome,peso,idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=False
        self.falando=False
        self.dormindo=False

    def comer (self):
        if self.falando==True:
            print(f"{self.nome} não pode comer pois ele/a está falando.")
        else:
            if self.dormindo==True:
                print(f"{self.nome} não pode comer pois ele/a está dormindo.")
            else:
                if self.comendo == False:
                    self.comendo = True
                    print(f"{self.nome} foi comer")
                else:
                    print(f"{self.nome} já estava comendo")

    def parardecomer (self):
        if self.comendo==True:
            self.comendo= False
            print(f"{self.nome} parou de comer.")
        else:
            print(f"{self.nome} já não estava comendo.")



    def falar (self):
        if self.comendo==True:
            print(f"{self.nome} não pode falar pois ele/a está comendo.")
        else:
            if self.dormindo==True:
                print(f"{self.nome} não pode falar pois ele/a está dormindo.")
            else:
                if self.falando==False:
                    self.falando=True
                    print(f"{self.nome} foi falar")
                else:
                    print(f"{self.nome} já estava falando")

    def parardefalar(self):
        if self.falando==True:
            self.falando=False
            print(f"{self.nome} parou de falar")
        else:
            print(f"{self.nome} já não estava falando")



    def dormir (self):
        if self.comendo==True:
            print(f"{self.nome} não pode dormir, pois ele/a está comendo.")
        else:
            if self.falando == True:
                print(f"{self.nome} não pode dormir, pois ele/a está falando.")
            else:
                if self.dormindo == False:
                    self.dormindo = True
                    print(f"{self.nome} foi dormir.")

                else:
                    print(f"{self.nome} já estava dormindo.")

    def parardedormir (self):
        if self.dormindo==True:
            self.dormindo=False
            print(f"{self.nome} acordou.")
        else:
            print(f"{self.nome} já estava acordado.")

