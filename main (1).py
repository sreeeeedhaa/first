from kivymd.app import MDApp
from kivy.lang import Builder


class Test(MDApp):
    def build(self):
        self.title = 'Soorarai pottru team'
        self.theme_cls.primary_palette = "Brown"
        return Builder.load_string(

            '''            
BoxLayout:
    orientation:'vertical'
    MDToolbar:
        title: 'Soorarai pottru team'
        md_bg_color: app.theme_cls.primary_color
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Nedumaran'

            Image:
                id: imageview
                source: 'Nedumaran.jpg'

    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Sebi'

            Image:
                id: imageview
                source: 'Sebi.jpg'


    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Cha'

            Image:
                id: imageview
                source: 'Cha.jpg'  
'''
        )


Test().run()
