import pyautogui as auto
from time import sleep
from googletrans import Translator as Tl
import pyperclip as clip

class Auto_Add_Cards():
    """Classe que representa automação na adição de cards"""
    def __init__(self, texts:str):
        self.texts = texts
        self.translation = Tl()


    def Creat_textlist(self):
        """chama cada frase ou palavra de texts.
            As frases ou palavras devem ter seu final delimitado por uma virgula ','.
            chama todas as funçoes do processo de automação para cada frase e palavra """
        for self.phrase in self.texts.split(";"):
            auto.sleep(1)
            self.front_input()
            self.audio()
            self.back_input()
            self.add_card()


    def translator(self):
        """Traduz a frase ou palavra da lista e retorna a mesma em formato de texto."""
        return self.translation.translate(self.phrase, dest="pt").text


    def front_input(self):
        """Cola as frases ou palavras no campo de entrada front"""
        clip.copy(self.phrase)
        auto.hotkey("ctrl", "v")


    def audio(self):
        """clica no botão do autofalante, depois clica em record para criar um 
           audio da frase ou palavra em ingles"""
        auto.hotkey("ctrl", "t")
        sleep(0.5)
        auto.press("tab")
        auto.press("tab")
        auto.press("enter")


    def back_input(self):
        """Clica e cola a tradução da frase ou palavra no campo de entrada back """
        sleep(0.7)
        auto.press("tab")
        clip.copy(self.translator())
        sleep(0.5)
        auto.hotkey("ctrlright", "v")
    

    def add_card(self):
        """Adiciona o cartão feito ao deck"""
        sleep(0.5)
        auto.hotkey("ctrl", "enter")
        sleep(1)


    def start(self):
        """Inicia a automação"""
        self.Creat_textlist()
#copyright ErykTavares © 2021