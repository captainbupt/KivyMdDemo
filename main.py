from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.toolbar import Toolbar
from kivymd.theming import ThemeManager
from kivy.properties import ObjectProperty
from kivymd.navigationdrawer import NavigationDrawer, NavigationDrawerIconButton
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.textfields import SingleLineTextField
from kivymd.button import MDFlatButton, MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.selectioncontrols import MDCheckbox, MDSwitch


class MyToolbar(Toolbar):
    def callback(self, x):
        # print type(App.get_running_app())
        print("here we go")
        App.get_running_app().show_example_dialog()
        pass

    def __init__(self, **kwargs):
        super(MyToolbar, self).__init__(**kwargs)
        self.title = "This is a pretty demo page"
        # self.left_action_items.append(['menu', self.callback])
        self.left_action_items.append(['menu', self.callback])


class MyNavDrawer(NavigationDrawer):
    def __init__(self, **kwargs):
        super(MyNavDrawer, self).__init__(**kwargs)
        self.title = "A pretty menu"
        self.add_widget(NavigationDrawerIconButton(icon='circle'))


class MyScreen(Screen):
    def __init__(self, **kwargs):
        super(MyScreen, self).__init__(**kwargs)
        scrollView = ScrollView()
        self.add_widget(scrollView)

        boxLayout = BoxLayout(orientation='vertical', height=dp(1000), padding=dp(48))
        scrollView.add_widget(boxLayout)
        textField = SingleLineTextField(id='text_filed', size_hint=(0.8, None), height=dp(48))
        textField.hint_text='This is a pretty text filed'
        boxLayout.add_widget(textField)
        buttonContainer = BoxLayout(orientation='horizontal', height=dp(48))
        flatButton = MDFlatButton(text='FlatButton')
        # size is not working somehow
        # flatButton.size = (3*dp(48), dp(48))
        buttonContainer.add_widget(flatButton)
        raiseButton = MDRaisedButton(text='RaiseButton')
        # raiseButton.size = (3*dp(48), dp(48))
        buttonContainer.add_widget(raiseButton)
        boxLayout.add_widget(buttonContainer)

        switchContainer = BoxLayout(orientation='horizontal')
        checkbox1 = MDCheckbox(group='test')
        # checkbox1.size=(dp(48), dp(48))
        switchContainer.add_widget(checkbox1)
        checkbox2 = MDCheckbox(group='test')
        # checkbox2.size=(dp(48), dp(48))
        switchContainer.add_widget(checkbox2)
        boxLayout.add_widget(switchContainer)



class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.add_widget(MyScreen(name='Screen 1'))
        self.current = 'Screen 1'


class RootScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(RootScreen, self).__init__(**kwargs)
        # self.nav_drawer = MyNavDrawer()
        # self.add_widget(self.nav_drawer)
        self.orientation = 'vertical'
        self.add_widget(MyToolbar())
        self.add_widget(MyScreenManager())


class MyApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        print('here we start')
        # self.theme_cls.theme_style = 'Dark'
        # self.show_example_dialog()
        # self.show_menu()
        return RootScreen()

    def test(self):
        print('here we go')

    def show_menu(self):
        self.nav_drawer = MyNavDrawer()
        self.nav_drawer.toggle()

    def show_example_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="This is a dialog with a title and some text. "
                               "That's pretty awesome right!",
                          valign='top')

        content.bind(size=content.setter('text_size'))
        self.dialog = MDDialog(title="This is a pretty dialog",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=False)

        self.dialog.add_action_button("Dismiss",
                                      action=lambda
                                          *x: self.dialog.dismiss())
        self.dialog.open()

if __name__ == '__main__':
    MyApp().run()
