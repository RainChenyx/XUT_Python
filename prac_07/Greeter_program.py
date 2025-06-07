from kivy.app import App
from kivy.lang import Builder


class GreeterProgram(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Greeter Program"
        self.root = Builder.load_file('Greeter_Program.kv')
        return self.root

    def handle_clear(self):
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text


GreeterProgram().run()
