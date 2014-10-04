from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class Strikkeapp(Screen):
    pass

class MainScreenManager(ScreenManager):
    pass

class Strikkemain(App):
    sa=Strikkeapp()
    def build(self):
	return Builder.load_file('strikke.kv')

Strikkemain().run()


