from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

COLOUR = (0, 0, 1, 1)


class DynamicWidgetsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Label"
        self.root = Builder.load_file('dynamic_label.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            temp_label.color = (1, 1, 1, 1)
            self.root.ids.name.add_widget(temp_label)
            number = self.name_to_phone[name]
            temp_label = Label(text=number)
            temp_label.color = (0, 1, 1, 1)
            self.root.ids.number.add_widget(temp_label)


DynamicWidgetsApp().run()
