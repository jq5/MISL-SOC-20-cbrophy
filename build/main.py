# Import libraries
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast


# Loading Windows
class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class SecondaryWindow(Screen):
    pass


class FillerName(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            previous=True,
        )

    def build(self):
        return Builder.load_file("layout.kv")

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

# Run Application
if __name__ == "__main__":
    FillerName().run()