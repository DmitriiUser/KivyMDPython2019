from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import pytube

class MainWindow(Screen):
        pass
        
class DownloadLayout(Screen):
        def download_url(self):
                url = self.ids.url_input.text

class PlaylistLayout(Screen):
        pass

class WindowManager(ScreenManager):
        pass

# Designate Our .kv design file 
kv = Builder.load_file('music.kv')
                
class MusicApp(App):
	def build(self):
		return kv

if __name__ == '__main__':
	MusicApp().run()
