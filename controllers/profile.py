from kivy.lang import Builder
from kivymd.app import MDApp as App
from kivymd.uix.screen import MDScreen


class HomeMainScreen(MDScreen):
    Builder.load_file('views/profile.kv', 'utf-8')


class HomeScreenApp(App):
    def build(self):
        return HomeMainScreen()


def main():
    HomeScreenApp().run()


if __name__ == '__main__':
    main()
