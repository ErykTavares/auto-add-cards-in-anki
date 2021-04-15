import PySimpleGUI as sg
from models.auto_deck import Auto_Add_Cards


class Window():
    def __init__(self):
        sg.theme("reddit")

        self.layout = [[sg.Text("Palavras/Frases", font="Verdanabold")],
                  [sg.Multiline(size=(30, 7), font="Verdanabold", key="-texts-")],
                  [sg.Button("Start", font="Verdanabold")]
        ]

        self.window = sg.Window("Auto add cards in anki", layout=self.layout, element_justification="c")

        while True:
            self.event, self.values = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
            if self.event == "Start":
                text = self.values["-texts-"]
                add_cards = Auto_Add_Cards(text)
                add_cards.start()
                sg.popup_ok("Cards Adicionados", font="Verdanabold", auto_close_duration=5000)
                
window = Window()
#copyright ErykTavares © 2021            