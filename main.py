from kivy.graphics.svg import Svg
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

Builder.load_file("openscreen.kv")

class OpenScreen(MDScreen):
    def ask_permission(self):
        self.ids.ask_permission.source = 'images/Permission_Granted.png'

class MyApp(MDApp):
    def build(self):
        return OpenScreen()


if __name__ == "__main__":
    MyApp().run()
