from kivymd.app import MDApp
from kivy.lang import Builder

from manager.navigation import NavigationManager


class MainScreenManager(NavigationManager):
    Builder.load_file('main.kv', 'utf-8')


class AlphaConnectApp(MDApp):
    def build(self):
        return MainScreenManager()

    def on_start(self):
        pass


if __name__ == '__main__':
    AlphaConnectApp().run()
