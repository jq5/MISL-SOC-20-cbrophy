from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Design(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def pressed(self):
        print(f"Name:  {self.name.text}\nEmail: {self.email.text}")
        self.name.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return Design()


if __name__ == "__main__":
    MyApp().run()