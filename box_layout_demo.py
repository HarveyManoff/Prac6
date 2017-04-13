from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def clear_handle_pressed(self):
        self.root.ids.output_text.text = ""
        self.root.ids.input_name.text = ""

        return

    def great_handle_pressed(self):
        self.root.ids.output_text.text = "Hello " + self.root.ids.input_name.text

        return



BoxLayoutDemo().run()
