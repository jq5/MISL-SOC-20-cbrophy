from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Design(GridLayout):
    def __init__(self, **kwargs):
        super(Design, self).__init__(**kwargs)
        self.inside = GridLayout()
        self.cols = 1

        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.firstName = TextInput(multiline=False)
        self.inside.add_widget(self.firstName)

        self.inside.add_widget(Label(text="Last name: "))
        self.surName = TextInput(multiline=False)
        self.inside.add_widget(self.surName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.firstName.text
        last = self.surName.text
        email = self.email.text

        print("Name:", name, "Last name:", last, "Email:", email)

        self.firstName.text = ""
        self.surName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return Design()

if __name__ == "__main__":
    MyApp().run()