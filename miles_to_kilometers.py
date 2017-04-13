from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometers(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Miles converter"
        self.root = Builder.load_file('miles_kivvy.kv')
        return self.root

    def handle_calculate(self, value):

        """ handle calculation (could be button press or other call), output result to label widget """
        #try:

        result = self.valid_number_check() * 1.6093
        self.root.ids.output_label.text = str(result)
        print(result)
        #except: ValueError


    def handle_increment(self, value_change):
        value = self.valid_number_check()
        value += value_change
        self.root.ids.input_number.text = str(value)

        print(value)

    def valid_number_check(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKilometers().run()
