import PySimpleGUI as sg
from models.auto_deck import Auto_Add_Cards
import clipboard


class Window():
    def __init__(self):
        sg.theme("reddit")

        self.rmb_menu = ["&Right", ["---", "Colar", "---"] ]

        self.layout = [[sg.Text("Palavras/Frases", font="Verdanabold")],
                  [sg.Multiline("texto ou frase aqui", tooltip="lembrando que toda frase exceto a primeira devera ter um ; na frente dela",size=(480, 17 ), font="Verdanabold", key="-texts-")],
                  [sg.Button("Start", font="Verdanabold")]
        ]

        self.window = sg.Window("Auto add cards in anki",size=(500, 400), layout=self.layout, element_justification="c", right_click_menu=self.rmb_menu)

        while True:
            self.event, self.values = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
            if self.event == "Colar":
               text =  str(clipboard.paste())
               self.window["-texts-"].Widget.insert("insert", text)
            if self.event == "Start":
                text = self.values["-texts-"]
                add_cards = Auto_Add_Cards(text)
                add_cards.start()
                sg.popup_ok("Cards Adicionados", font="Verdanabold", auto_close_duration=5000)
                
window = Window()
#copyright ErykTavares © 2021            