import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class myGridLayout(GridLayout):
    def doit(self,result):
        if result:
            try:
                self.display.text=str(eval(result))
            except:
                self.display.text="Error"


class caApp(App):
    def build(self):
        return myGridLayout()

caApp().run()