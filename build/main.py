# Import libraries
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App

# Loading Windows
class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class SecondaryWindow(Screen):
    pass


class FillerName(App):
    def build(self):
        return Builder.load_file("layout.kv")

# Run Application
if __name__ == "__main__":
    FillerName().run()