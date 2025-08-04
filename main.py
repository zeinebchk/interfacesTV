import socketio
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (900, 600)

sio = socketio.Client()


class MainApp(MDApp):
    compt=0
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        # Charge l'interface et stocke la référence
        self.root_widget = Builder.load_file("main.kv")
        sio.connect("http://127.0.0.1:5001")
        return self.root_widget

    def on_start(self):
        @sio.on("of_lance")
        def of_lance_handler(data):
            self.compt+=1
            print("Donnée reçue:", data)

            Clock.schedule_once(lambda dt: self.update_label(str(self.compt)))

    def update_label(self, text):
        if hasattr(self.root_widget, 'ids'):
            self.root_widget.ids.objectif_id.text = text


if __name__ == "__main__":
    MainApp().run()