from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp

KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Profile"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Diet"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
                    
            # OneLineListItem:
            #     text: "Pain Check"
            #     on_press:
            #         root.nav_drawer.set_state("close")
            #         root.screen_manager.current = "scr 3"
                    
            # OneLineListItem:
            #     text: "Search"
            #     on_press:
            #         root.nav_drawer.set_state("close")
            #         root.screen_manager.current = "scr 4"
                    
            OneLineListItem:
                text: "Info"
                
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 5"
                    
            OneLineListItem:
                text: "About Us"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 6"
                    
                    


Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        
        size_hint:(1,0.1)
        specific_text_color:1,1,1,1
        
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDLabel:
                    text: "Profile"
                    halign: "center"
                    
               

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Diet"
                    halign: "center"
                    
            Screen:
                name:"scr 3"
                
                MDLabel:
                    text:"Pain Check"
                    halign:"center"
                    
            Screen:
                name:"scr 4"
                
                MDLabel:
                    text:"Search"
                    halign:"center"
                    
            Screen:
                name:"scr 5"
                
                MDLabel:
                    text:"This App helps women who are going through preganancy without much knowledge about it.This app is basically guides women towards how to manage their body during this tough time."
                    font_size:20
                    pos_hint:{'center_x':0.5,'y':0.2}
                    halign:"center"
                    
                MDLabel:
                    text:"•We first take the contact details of the family members so that we can send them during any emergency arises  "
                    pos_hint:{'center_x':0.5,'y':0.0}
                    halign:"center"
                    
                MDLabel:
                    text:"•We schedule all 13 tests and other important check-ups and events essential during the preganancy into our calender so that it can be easily assesible to customer.All the upcoming events can be accessed through this section "
                    
                    pos_hint:{'center_x':0.5,'y':-0.15}
                    halign:"center"
                    
                MDLabel:
                    text:"•We also provide a chat room where other mothers can share their experience through blogs "
                    pos_hint:{'center_x':0.5,'y':-0.3}
                    halign:"center"
                
                MDLabel:
                    text:"•We also manage nutritient intake of the mother and provide necessary information about the calories and electrolyte intakes. "
                    pos_hint:{'center_x':0.5,'y':-0.45}
                    halign:"center"
                    
                    
            Screen:
                name:"scr 6"
                
                MDLabel:
                    text:"Efforts By  Avyav Sharma  ,  Harsh Jain  ,  Vidit Jain  "
                    
                     
                    halign:"center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)


TestNavigationDrawer().run()