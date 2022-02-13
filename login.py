from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class  MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        label4 = Label(text="Logo", bold=True, italic=True, size_hint=(0.2, 0.2))
        self.value1 = TextInput(text="Enter UserName", size_hint=(1, 0.02), height=20, width=400, font_size=15, padding=6)
        self.value  = TextInput(text="Enter Email" , size_hint=(1,0.02),height=20,width=400,font_size=15,padding=6)
        self.value2 = TextInput(text="Enter Password", size_hint=(1,0.02),height=20,width=400,font_size=15,padding=6)
        submit = Button(text='Login', size_hint=(1, 0.02), height=30, width=400, font_size=15, on_press=self.submit)

        layout.add_widget(label4)
        layout.add_widget(self.value1)
        layout.add_widget(self.value)
        layout.add_widget(self.value2)
        layout.add_widget(submit)
        return layout
    def submit(self,obj):
        print("UserName:" + self.value1.text)
        print("Email:" + self.value.text )
        print("Password:" + self.value2.text)
MainApp().run()