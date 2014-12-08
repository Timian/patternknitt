#main.py is the main file, that is used for running the application.
#imports diffrent function from kviy library.
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

#these two just activate the function to the screen,so we can see
class Strikkeapp(Screen):
    pass

class MainScreenManager(ScreenManager):
    pass

#loads the strikke.kv file(the design for the application) and build the strikkeapp
class Strikkemain(App):
    sa=Strikkeapp()
    def build(self):
	return Builder.load_file('strikke.kv')
#runs the application
Strikkemain().run()


