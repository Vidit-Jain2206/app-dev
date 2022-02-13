import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40 , spacing=10, padding=20)
        self.weight = TextInput(text=' enter food item')

        submit = Button(text='Submit', on_press=self.submit)
        layout.add_widget(self.weight)

        layout.add_widget(submit)
        layout.add_widget(Label(text="number of calories consumed today are 6250 calories"))

        return layout

    def submit(self,obj):
        print("weight:" + self.weight.text)
        print("height:" + self.height.text)
        a=self.weight.text
        print(a)


MainApp().run()


