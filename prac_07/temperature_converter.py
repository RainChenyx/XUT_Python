from kivy.app import App
from kivy.lang import Builder


class TemperatureConverter(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Temperature Converter Program"
        self.root = Builder.load_file('temperature_converter.kv')
        return self.root

    def handle_increment(self, change):
        value = self.get_validated_number() + change
        self.root.ids.input_number.text = str(value)

    def handle_calculate_fahrenheit(self):
        celsius = self.get_validated_number()
        if celsius == -999:
            self.root.ids.output_label.text = "Invalid number, please re-enter the correct number."
        else:
            fahrenheit = celsius * 9.0 / 5 + 32
            self.root.ids.output_label.text = str(fahrenheit)

    def handle_calculate_celsius(self):
        fahrenheit = self.get_validated_number()
        if fahrenheit == -999:
            self.root.ids.output_label.text = "Invalid number, please re-enter the correct number."
        else:
            celsius = 5 / 9 * (fahrenheit - 32)
            self.root.ids.output_label.text = str(celsius)

    def get_validated_number(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return -999


TemperatureConverter().run()
