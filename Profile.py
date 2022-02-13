from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainApp(App):
    def build(self):

        layout = BoxLayout(orientation='vertical',spacing=10,padding=20)
        label  = Label(text="Username - Mohini290", bold=True,italic=True,size_hint=(0.2,0.2))
        label2 = Label(text=" Email - mohine@gmail.com", bold=True, italic=True, size_hint=(0.2, 0.2), )
        label3 = Label(text="Emergency contact", bold=True, italic=True, size_hint=(0.2, 0.2), )
        Addemer = Button(text="Add New Contact",size_hint=(0.17,0.17),font_size=14 )
        label4 = Label(text="Change Password", bold=True, italic=True, size_hint=(0.2, 0.2),)
        label5 = Label(text="Relation - Husband", bold=True, italic=True, size_hint=(0.2, 0.2), )
        label6 = Label(text="Name-Rohit", bold=True, italic=True, size_hint=(0.2, 0.2), )
        label7 = Label(text="Phone No. - 9765432102", bold=True, italic=True, size_hint=(0.2, 0.2), )
        self.value4 = TextInput(text="Enter Current Password", size_hint=(1,0.13),height=30,width=400,font_size=15,padding=6 )
        self.value5 = TextInput(text="Enter New Password", size_hint=(1,0.13),height=30,width=400,font_size=15,padding=6)
        submit = Button(text='Submit',size_hint=(1,0.1),font_size=15,on_press=self.submit)
        layout.add_widget(label)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(Addemer)
        layout.add_widget(label5)

        layout.add_widget(label6)
        layout.add_widget(label7)
        layout.add_widget(label4)
        layout.add_widget(self.value4)
        layout.add_widget(self.value5)
        layout.add_widget(submit)


        return layout
    def submit(self,obj):

        print("Current Password.:" + self.value4.text)
        print("New Password:" + self.value5.text)



MainApp().run()

