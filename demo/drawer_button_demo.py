"""
MIT License
Copyright (c) 2019 Shashi Ranjan
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from kivy.animation import Animation

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.button import MDIconButton
from kivymd.theming import ThemeManager
from kivymd.elevation import RectangularElevationBehavior
from kivymd.navigationdrawer import NavigationLayout, MDNavigationDrawer

from kivy.properties import NumericProperty

kv="""
#:import MDLabel kivymd.label.MDLabel
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import MDSeparator kivymd.cards.MDSeparator

#:import C kivy.utils.get_color_from_hex

<DrawerButton>:
	canvas.before:
		PushMatrix
		Rotate:
			angle: self.angle
			origin: self.center
	canvas:
		PopMatrix

	pos_hint: {"center_x":0.5,"center_y":.5}
	theme_text_color:'Custom'
	text_color: 1,1,1,1
	icon:'menu'	


DemoLayout:
	orientation: 'vertical'
	MyToolBar:
		id: toolbar
		canvas:
			Color:
				rgba:C('#2874a6')
			Rectangle:
				pos: self.pos
				size: self.size

		elevation: 10
		size_hint: 1,None
		height: dp(60)
		title: "DrawerButton Demo"

		AnchorLayout:
			size_hint_x: None
			DrawerButton:
				id:btn
				on_release:
					nav_layout.toggle_nav_drawer()
					print(nav_drawer.pos)

		BoxLayout:
	        padding: dp(12), 0

	        MDLabel:
	            font_style: 'H6'
	            opposite_colors: toolbar.opposite_colors
	            theme_text_color: 'Custom'
	            text_color: toolbar.specific_text_color
	            text: toolbar.title
	            shorten: True
	            shorten_from: 'right'
	
	NavigationLayout:
		id: nav_layout
		anim_type: 'slide_above_anim'
		opening_transition: 'out_cubic'
		closing_transition: 'in_cubic'

		on_touch_down:
			if self.state=='open':root.set_btn(btn)

		MyNavDrawer:
			id: nav_drawer
			canvas:
				Color:
					rgb: C('#1c2833')
				Rectangle:
					pos: self.pos
					size: self.size
			elevation:10
			Label:
				text:"Nav contents here"
				color:1,1,1,1

		Label:
			text: "Content goes here"
			color:[0,0,0,1]

"""
class MyToolBar(BoxLayout,RectangularElevationBehavior):
	opposite_colors= False
	specific_text_color=[1,1,1,1]
	title=""

class MyNavDrawer(BoxLayout,RectangularElevationBehavior):
	pass

class DrawerButton(MDIconButton):
	angle= NumericProperty(0)

	def on_release(self):
		if self.angle in [0,-180,-360]:
			if self.angle==-360:
				self.angle=0

			ang=self.angle-90
			if self.icon=='menu':
				icon='arrow-right'
			else:
				icon='menu'

			anim=Animation(
				d=0.08,
				angle=ang
			)
			anim.bind(on_complete= lambda x,y:setattr(self, 'icon', icon))

			anim+=Animation(
				d=0.08,
				angle=ang-90,
			)
			anim.start(self)

class DemoLayout(BoxLayout):
	def set_btn(self,btn):
		if btn.angle in [0,-180,-360]:
			if btn.angle==-360:
				btn.angle=0

			ang=btn.angle-90
			if btn.icon=='menu':
				icon='arrow-right'
			else:
				icon='menu'

			anim=Animation(
				d=0.1,
				angle=ang
			)
			anim.bind(on_complete= lambda x,y:setattr(btn, 'icon', icon))

			anim+=Animation(
				d=0.1,
				angle=ang-90,
			)
			#anim.cancel_all(self)
			anim.start(btn)

class DrawerButtonDemo(App):
	theme_cls= ThemeManager()
	def build(self):
		return Builder.load_string(kv)

if __name__ == '__main__':
	DrawerButtonDemo().run()
