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
        text: 'Symboling'
        pos_hint: {'center_y':0.75}

    MDTextField:
        id: input_1
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.75, 'center_x':0.5}

    MDLabel:
        text: 'Fuel Type'
        pos_hint: {'center_y':0.68}

    MDTextField:
        id: input_2
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.68, 'center_x':0.5}

    MDLabel:
        text: 'Aspiration'
        pos_hint: {'center_y':0.61}

    MDTextField:
        id: input_3
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.61, 'center_x':0.5}

    MDLabel:
        text: 'Door Number'
        pos_hint: {'center_y':0.54}

    MDTextField:
        id: input_4
        hint_text: '(0.0 - 4)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.54, 'center_x':0.5}

    MDLabel:
        text: 'Car body'
        pos_hint: {'center_y':0.47}

    MDTextField:
        id: input_5
        hint_text: '(0.0 - 20.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.47, 'center_x':0.5}

    MDLabel:
        text: 'Drivewheel'
        pos_hint: {'center_y':0.40}

    MDTextField:
        id: input_6
        hint_text: '(0.0 - 1.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.40, 'center_x':0.5}

    MDLabel:
        text: 'Engine Location'
        pos_hint: {'center_y':0.33}

    MDTextField:
        id: input_7
        hint_text: '(0.0 - 2.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.33, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_8
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}
    
    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_9
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_10
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_11
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_12
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_13
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_14
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_15
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_16
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_17
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_18
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_19
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_20
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_21
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_22
        hint_text: '(0.0 - 3.0)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.26, 'center_x':0.5}

    MDLabel:
        text: 'Wheel Base'
        pos_hint: {'center_y':0.26}

    MDTextField:
        id: input_23
        hint_text: '(0.0 - 3.0)'
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
        url = f"https://carpriceapi.herokuapp.com/predict?acousticness={acousticness}&danceability={danceability}&energy={energy}&instrumentalness={instrumentalness}&liveness={liveness}&speechiness={speechiness}&tempo={tempo}&valence={valence}"
        self.request = UrlRequest(
            url=url, on_success=self.res, ca_file=cfi.where(), verify=True
        )

    def res(self, *args):
        self.data = self.request.result
        ans = self.data
        self.help_string.get_screen("main").ids.output_text.text = ans["prediction"]


MainApp().run()
