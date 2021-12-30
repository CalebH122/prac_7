from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Convertor(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


Convertor().run()
