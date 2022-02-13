from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        label2 = Label(text="Enter Emergency Contact", bold=True, italic=True, size_hint=(0.5, 0.4))
        self.value3 = TextInput(text="Enter Relation", size_hint=(1, 0.05), height=20, width=400, font_size=15,
                                padding=6)
        self.value4 = TextInput(text="Enter Name", size_hint=(1, 0.05), height=20, width=400, font_size=15, padding=6)
        self.value5 = TextInput(text="Enter Phone No.", size_hint=(1, 0.05), height=20, width=400, font_size=15,
                                padding=6)
        submit = Button(text='Submit', size_hint=(1, 0.05), font_size=15, on_press=self.submit)

        layout.add_widget(label2)
        layout.add_widget(self.value3)
        layout.add_widget(self.value4)
        layout.add_widget(self.value5)
        layout.add_widget(submit)

        return layout
    def submit(self,obj):
        print("Relation:" + self.value3.text)
        print("Name:" + self.value4.text)
        print("Phone No.:" + self.value5.text)
MainApp().run()
