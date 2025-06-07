from kivy.app import App
from kivy.lang import Builder


class Score(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Score Calculator"
        self.root = Builder.load_file('score.kv')
        return self.root

    def handle_clear(self):
        self.root.ids.input_score.text = ""
        self.root.ids.output_label.text = "Enter your score."

    def handle_calculate(self):
        score = self.get_validated_score()
        if score == -1:
            result = "Invalid, please enter a value number from 0 to 100."
        elif 85 <= score <= 100:
            result = "Pass with High Distinction"
        elif 75 <= score < 85:
            result = "Pass with Distinction"
        elif 65 <= score < 75:
            result = "Pass with Credit"
        elif 50 <= score < 65:
            result = "Pass"
        elif 0 <= score < 50:
            result = "Fail"
        else:
            result = "Invalid, please enter a value number from 0 to 100."
        self.root.ids.output_label.text = result

    def get_validated_score(self):
        try:
            value = float(self.root.ids.input_score.text)
            return value
        except ValueError:
            return -1


Score().run()
