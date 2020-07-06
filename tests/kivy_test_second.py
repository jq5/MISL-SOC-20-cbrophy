from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.lang import Builder

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, .5, mode="rgba")
            self.rec = Rectangle(pos=(0,0), size=(50,50))

    def on_touch_down(self, touch):
        print("mouse down", touch)
        self.rec.pos = touch.pos

    def on_touch_move(self, touch):
        print("mouse move", touch)
        self.rec.pos = touch.pos

class Second(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    Second().run()