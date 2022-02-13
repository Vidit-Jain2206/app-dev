# python file


from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker, MDDatePicker


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('bbar.kv')

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.open()


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


MainApp().run()
