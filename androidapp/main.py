from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
import certifi as cfi

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import webbrowser
import certifi as cfi


kv = '''
<MainScreen>:
    name: "Main-Layout"
    number: number
    NavigationLayout:
        ScreenManager:
            id: screen_manager
            Screen:
                name: "home-screen"
                MDLabel:
                    text: "[b]Welcome to IPU Results App[/b]"
                    halign: "center"
                    font_style: "H4"
                    markup: True
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Home"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12
                    Widget:
            Screen:
                name: "about-screen"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "About"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12
                    Widget:
                MDLabel:
                    text: "This app is made as an [b]extension to the current website[/b] and [b]telegram bot[/b].[i] Using this app you can fetch your results which usually come in the form of long PDFs which are difficult to analyse. There are numerous columns with different subject codes which often confuses the student. We aim to resolve this difficulty and make your experience better[/i]. [b]New features, data and functionality will be added as the app progress[/b]. Feel free to drop any message related to any discrepancy or any other suggestion. Check out the contact tab for that."
                    halign: "center"
                    markup: True
            Screen:
                name: "contact-screen"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Contact"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12
                    Widget:
                BoxLayout:
                    orientation: "vertical"
                    MDLabel:
                        text: ""
                    MDList:
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://www.instagram.com/kaustubhgupta1828/")
                            text: "Instagram"
                            IconLeftWidget:
                                icon: "instagram"
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://www.facebook.com/kaustubh.gupta.1828/")
                            text: "Facebook"
                            IconLeftWidget:
                                icon: 'facebook'
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://twitter.com/Kaustubh1828")
                            text: "Twitter"
                            IconLeftWidget:
                                icon: "twitter"
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://www.linkedin.com/in/kaustubh-gupta-612767ab/")
                            text: "Linkedin"
                            IconLeftWidget:
                                icon: "linkedin"
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://github.com/kaustubhgupta")
                            text: "GitHub"
                            IconLeftWidget:
                                icon: "gitlab"
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://medium.com/@kaustubhgupta1828")
                            text: "Medium"
                            IconLeftWidget:
                                icon: "medium"
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://www.kaustubhgupta.xyz/")
                            text: "Personal Blogging Website"
                            IconLeftWidget:
                                icon: "web"
                    Widget:
            Screen:
                name: "result-screen"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Result"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12
                    Widget:
                MDLabel:
                    halign: "center"
                    text: "[b]Marks Summary[/b]"
                    markup: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                    font_style: "H6"
                MDLabel:
                    id: other_info
                    halign: "center"
                    text: ""
                    markup: True
                MDRectangleFlatButton:
                    text: 'Marks'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_press: root.datatables.open()
            Screen:
                name: "input-screen"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "Result"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation :12
                    Widget:
                MDTextField:
                    id: number
                    hint_text: "Enter your enrollment number"
                    helper_text_mode: "on_focus"
                    icon_right: "account-search"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: None
                    width: 300
                    required: True
                MDRaisedButton:
                    id: drop_semester
                    pos_hint: {'center_x': .6, 'center_y': .4}
                    text: 'Semester'
                    on_release: root.menu_semester.open()
                MDRaisedButton:
                    id: drop_batch
                    pos_hint: {'center_x': .36, 'center_y': .4}
                    text: 'Batch'
                    on_release: root.menu_batch.open()
                MDRectangleFlatButton:
                    text: 'Submit'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_press:
                        root.btn()
                MDLabel:
                    id: loading
                    haling: 'center'
                    text: ''
                    font_style: "H4"
                    theme_text_color: 'Custom'
                    text_color: (1, 0, 0, 1)
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                spacing: '8dp'
                padding: '8dp'
                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height: avatar.height
                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: "logo.png"
                MDLabel:
                    text: "IPU Results App"
                    font_style: "H4"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "From the Creator of IPUResults Website & IPUTelegrambot"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineAvatarListItem:
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "home-screen"
                            text: "Home"
                            IconLeftWidget:
                                icon: "home"
                        OneLineAvatarListItem:
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "about-screen"
                            text: "About"
                            IconLeftWidget:
                                icon: 'information'
                        OneLineAvatarListItem:
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "input-screen"
                            text: "Check Results"
                            IconLeftWidget:
                                icon: "account-search"
                        OneLineAvatarListItem:
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "contact-screen"
                            text: "Contact"
                            IconLeftWidget:
                                icon: "contacts"
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://carflaskpred.herokuapp.com/")
                            text: "Visit website"
                            IconLeftWidget:
                                icon: "web"
                        OneLineAvatarListItem:
                            on_press: root.openweb("https://t.me/ipuBOT")
                            text: "Telegram Bot"
                            IconLeftWidget:
                                icon: "telegram"
'''



Builder_string = """
ScreenManager:
    Main:
<Main>:


    name : 'main'
    MDLabel:
        text: 'Car Price Prediction App'
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H3'

    MDLabel:
        text: 'Acousticness'
        pos_hint: {'center_y':0.75}

    MDTextField:
        id: input_1
        hint_text: '(0.0000009491 - 0.9957965)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.75, 'center_x':0.5}

    MDLabel:
        text: 'Danceability'
        pos_hint: {'center_y':0.68}

    MDTextField:
        id: input_2
        hint_text: '(0.051307 - 0.961871)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.68, 'center_x':0.5}

    MDLabel:
        text: 'Energy'
        pos_hint: {'center_y':0.61}

    MDTextField:
        id: input_3
        hint_text: '(0.000279 - 0.999768)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.61, 'center_x':0.5}

    MDLabel:
        text: 'Instrumentalness'
        pos_hint: {'center_y':0.54}

    MDTextField:
        id: input_4
        hint_text: '(0 - 0.993134)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.54, 'center_x':0.5}

    MDLabel:
        text: 'Liveness'
        pos_hint: {'center_y':0.47}

    MDTextField:
        id: input_5
        hint_text: '(0.025297 - 0.971392)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.47, 'center_x':0.5}

    MDLabel:
        text: 'Speechiness'
        pos_hint: {'center_y':0.40}

    MDTextField:
        id: input_6
        hint_text: '(0.023234 - 0.966177)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.40, 'center_x':0.5}

    MDLabel:
        text: 'Tempo'
        pos_hint: {'center_y':0.33}

    MDTextField:
        id: input_7
        hint_text: '(29.093000 - 250.059000)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.33, 'center_x':0.5}

    MDLabel:
        text: 'Valence'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_8
        hint_text: '(0.014392 - 0.983649)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        pos_hint: {'center_y':0.2}
        halign: 'center'
        text: ''
        id: output_text
        theme_text_color: "Custom"
        text_color: 0, 1, 0, 1

    MDRaisedButton:
        pos_hint: {'center_x':0.5, 'center_y':0.1}
        text: 'Predict'
        on_press: app.predict()
"""


class Main(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Main(name="main"))


class MainApp(MDApp):
    def build(self):
        self.help_string = Builder.load_string(Builder_string)
        return self.help_string

    def predict(self):
        acousticness = self.help_string.get_screen("main").ids.input_1.text
        danceability = self.help_string.get_screen("main").ids.input_2.text
        energy = self.help_string.get_screen("main").ids.input_3.text
        instrumentalness = self.help_string.get_screen("main").ids.input_4.text
        liveness = self.help_string.get_screen("main").ids.input_5.text
        speechiness = self.help_string.get_screen("main").ids.input_6.text
        tempo = self.help_string.get_screen("main").ids.input_7.text
        valence = self.help_string.get_screen("main").ids.input_8.text
        url = f"https://https://carpriceapi.herokuapp.com//predict?acousticness={acousticness}&danceability={danceability}&energy={energy}&instrumentalness={instrumentalness}&liveness={liveness}&speechiness={speechiness}&tempo={tempo}&valence={valence}"
        self.request = UrlRequest(
            url=url, on_success=self.res, ca_file=cfi.where(), verify=True
        )

    def res(self, *args):
        self.data = self.request.result
        ans = self.data
        self.help_string.get_screen("main").ids.output_text.text = ans["prediction"]


MainApp().run()
