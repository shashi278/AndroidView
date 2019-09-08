import sys
sys.path.append('../')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.clock import Clock

import time

from button.wirelessripplebutton import WirelessRippleButton,render

kv="""

<DemoButton>:

	size_hint: None, None
	size: 50,50
	pos_hint: {"center_x":.35, "center_y":.7}

	#opacity:0

	canvas.after:
		Color:
			rgba: [1,1,1] + [1]
		Ellipse:
			source: "phone2.png"
			pos: self.x-((self.size[0]*1.5)/2-self.size[0]/2) ,self.y-((self.size[0]*1.5)/2-self.size[0]/2)
			size: self.size[0]*1.5, self.size[0]*1.5

DemoLayout:
	canvas:
		Color:
			rgba:1,1,1,1
		Rectangle:
			pos: self.pos
			size: self.size
	MyButton:
		pos_hint: {"center_x":.5, "center_y":.5}

		on_release:
			root.on_release()



"""

class DemoButton(Button):
	pass

class DemoLayout(FloatLayout):
	def on_release(self, *args):
		Clock.schedule_once(self.add_btn,3)
	
	def add_btn(self,_):
		demoBtn= DemoButton()
		self.add_widget(demoBtn)

class MyButton(WirelessRippleButton):
	pass

class DemoApp(App):
	def build(self):
		return Builder.load_string(kv+render)

if __name__ == '__main__':
	DemoApp().run()