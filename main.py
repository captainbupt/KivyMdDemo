from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.toolbar import Toolbar
from kivymd.theming import ThemeManager
from kivy.properties import ObjectProperty
from kivymd.navigationdrawer import NavigationDrawer, NavigationDrawerIconButton
from kivy.uix.screenmanager import ScreenManager, Screen

class MyToolbar(Toolbar):

    def callback(self, x):
        #print("test:" + x)
        pass

    def __init__(self, **kwargs):
        super(MyToolbar, self).__init__(**kwargs)
        self.title = "This is a pretty demo page"
        #self.left_action_items.append(['menu', self.callback])
        self.left_action_items.append(['menu', lambda x : App.get_running_app().test])


class MyNavDrawer(NavigationDrawer):

    def __init__(self, **kwargs):
        super(MyNavDrawer, self).__init__(**kwargs)
        self.title = "A pretty menu"
        self.add_widget(NavigationDrawerIconButton(icon='circle'))


class MyScreenManager(ScreenManager):


class RootScreen(BoxLayout):

    nav_drawer = ObjectProperty()

    def __init__(self, **kwargs):
        super(RootScreen, self).__init__(**kwargs)
        #self.nav_drawer = MyNavDrawer()
        #self.add_widget(self.nav_drawer)
        self.orientation = 'vertical'
        self.add_widget(MyToolbar())
        self.add_widget(Label(text='User Name'))


class MyApp(App):

    theme_cls = ThemeManager()

    def build(self):
        print('here we start')
        #self.theme_cls.theme_style = 'Dark'
        return RootScreen()

    def test(self):
        print('here we go')

if __name__ == '__main__':
    MyApp().run()