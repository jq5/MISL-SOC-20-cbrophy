from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0/fps)
        print("Initialised...")

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Convert to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]),
                colorfmt="bgr"
            )
            image_texture.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
            # Display image from the texture
            self.texture = image_texture
            print("Updated Image...")

class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(1)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        print("Built Camera...")
        return self.my_camera

    def on_stop(self):
        # App won't exit even if closed without this
        self.capture.release()

if __name__ == "__main__":
    CamApp().run()
    cv2.destroyAllWindows()
