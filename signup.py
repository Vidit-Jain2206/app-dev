from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class  MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        label1 = Label(text="Logo", bold=True, italic=True, size_hint=(0.4, 0.4))
        self.value1 = TextInput(text="Enter UserName", size_hint=(1, 0.05), height=20, width=400, font_size=15, padding=6)
        self.value2  = TextInput(text="Enter Email" , size_hint=(1,0.05),height=20,width=400,font_size=15,padding=6)
        label2 = Label(text="Enter Emergency Contact", bold=True, italic=True,size_hint=(0.5,0.1))
        self.value3 = TextInput(text="Enter Relation", size_hint=(1, 0.05), height=20, width=400, font_size=15, padding=6)
        self.value4 = TextInput(text="Enter Name", size_hint=(1, 0.05), height=20, width=400, font_size=15, padding=6)
        self.value5 = TextInput(text="Enter Phone No.", size_hint=(1, 0.05), height=20, width=400, font_size=15, padding=6)
        self.value6 = TextInput(text="Enter Password", size_hint=(1,0.05),height=20,width=400,font_size=15,padding=6)
        submit = Button(text='SignUp', size_hint=(1, 0.05), font_size=15, on_press=self.submit)

        layout.add_widget(label1)
        layout.add_widget(self.value1)
        layout.add_widget(self.value2)
        layout.add_widget(label2)
        layout.add_widget(self.value3)
        layout.add_widget(self.value4)
        layout.add_widget(self.value5)
        layout.add_widget(self.value6)
        layout.add_widget(submit)
        return layout
    def submit(self,obj):
        print("UserName:" + self.value1.text)
        print("Email:" + self.value2.text)
        print("Relation:" + self.value3.text)
        print("Name:" + self.value4.text)
        print("Phone No.:" + self.value5.text)
        print("Password:" + self.value6.text)

MainApp().run()