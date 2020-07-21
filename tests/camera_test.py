from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera


class Main(BoxLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)

        self.cols = 1

        self.add_widget(Camera(
            index=1,
            play=True
        ))


class CameraApp(App):
    def build(self):
        return Main()


if __name__ == "__main__":
    CameraApp().run()
