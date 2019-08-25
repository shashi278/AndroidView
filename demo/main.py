import sys
sys.path.append('../')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivymd.theming import ThemeManager

from functools import partial

from animator.attention import *
from animator.bouncein import *
from animator.fadein import *
from animator.fadeout import *
from animator.rotatein import *
from animator.rotateout import *
from animator.slidein import *
from animator.slideout import *
from animator.zoomin import *
from animator.zoomout import *
from animator.extra import *


kv="""
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import C kivy.utils.get_color_from_hex
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem

<ListItem@OneLineListItem>:
	theme_text_color: 'Custom'
	text_color: [1,1,1,1]
	bold: True

MyLabel:
	orientation: "vertical"
	
	FloatLayout:
		size_hint_y: .4

		AnchorLayout:
			pos_hint: {"center_x":0.5, "center_y": 0.5}
			size_hint: None, None
			#size: (250,60)
			size: self.parent.width/2, self.parent.height/2
			opacity:1
			angle: 0
			origin_: None
			axis: tuple((0,0,1))
			

			canvas.before:
				PushMatrix
				Rotate:
					axis: self.axis
					angle: self.angle 
					origin: self.origin_ or self.center

				Color:
					rgba: 1,1,0,0
				Rectangle:
					pos: self.pos
					size: self.size
			canvas.after:
				PopMatrix

			Label:
				size_hint: None, None
				size: self.texture_size
				id: lbl
				text: "Hello Kivy!"
				color: 0,0,0,1
				font_size: min(self.parent.height/1.3, self.parent.width/5)
				opacity: 1
				padding: 5,5


	ScrollView:
		do_scroll_x: False

		canvas.before:
			Color:
				rgb:C('#4a235a')
			Rectangle:
				pos: self.pos
				size: self.size
		
		MDList:
			ListItem:
				text:"FlashAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"PulseAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RubberBandAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"ShakeAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"SwingAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"WobbleAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"TadaAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"WaveAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)

			ListItem:
				text:"BounceInAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"BounceInDownAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"BounceInLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"BounceInRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"BounceInUpAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)

			ListItem:
				text:"FadeInAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"FadeInDownAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"FadeInLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"FadeInRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"FadeInUpAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)

			ListItem:
				text:"FadeOutAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"FadeOutDownAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"FadeOutLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"FadeOutRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"FadeOutUpAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)

			ListItem:
				text:"RotateInAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RotateInDownLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RotateInDownRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RotateInUpLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RotateInUpRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)

			ListItem:
				text:"RotateOutAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RotateOutDownLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RotateOutDownRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RotateOutUpLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RotateOutUpRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)

			ListItem:
				text:"SlideInDownAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"SlideInLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"SlideInRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"SlideInUpAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)

			ListItem:
				text:"SlideOutDownAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"SlideOutLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"SlideOutRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"SlideOutUpAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
	
			ListItem:
				text:"ZoomInAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"ZoomInDownAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"ZoomInLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"ZoomInRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"ZoomInUpAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)

			ListItem:
				text:"ZoomOutAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"ZoomOutDownAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"ZoomOutLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"ZoomOutRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"ZoomOutUpAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)

			ListItem:
				text:"FlyInAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"FlyOutAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"DropOutAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"HingLeftAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"HingRightAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RollInAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
			ListItem:
				text:"RollOutAnimator"
				on_release:
					root.animate(root.ids.lbl.parent, self.text)
		
"""

class MyLabel(BoxLayout):
	defaults={
		'pos_hint': {"center_x":0.5, "center_y": 0.5},
		'size': '',
		'opacity':1,
		'angle': 0,
		'origin_':''}

	def reset(self, widget):
		for key, val in self.defaults.items():
			if key=='size':
				val=(widget.parent.width/2, widget.parent.height/2)
			setattr(widget, key, val)

	def animate(self, widget, anim_name):
		self.reset(widget)
		if anim_name=="FlashAnimator": FlashAnimator(widget).start_()
		if anim_name=="PulseAnimator": PulseAnimator(widget).start_()
		if anim_name=="RubberBandAnimator": RubberBandAnimator(widget).start_()
		if anim_name=="ShakeAnimator": ShakeAnimator(widget).start_()
		if anim_name=="SwingAnimator": SwingAnimator(widget).start_()
		if anim_name=="WobbleAnimator": WobbleAnimator(widget).start_()
		if anim_name=="TadaAnimator": TadaAnimator(widget).start_()
		if anim_name=="WaveAnimator": WaveAnimator(widget).start_()

		if anim_name=="BounceInAnimator": BounceInAnimator(widget).start_()
		if anim_name=="BounceInDownAnimator": BounceInDownAnimator(widget).start_()
		if anim_name=="BounceInLeftAnimator": BounceInLeftAnimator(widget).start_()
		if anim_name=="BounceInRightAnimator": BounceInRightAnimator(widget).start_()
		if anim_name=="BounceInUpAnimator": BounceInUpAnimator(widget).start_()

		if anim_name=="FadeInAnimator": FadeInAnimator(widget).start_()
		if anim_name=="FadeInDownAnimator": FadeInDownAnimator(widget).start_()
		if anim_name=="FadeInLeftAnimator": FadeInLeftAnimator(widget).start_()
		if anim_name=="FadeInRightAnimator": FadeInRightAnimator(widget).start_()
		if anim_name=="FadeInUpAnimator": FadeInUpAnimator(widget).start_()

		if anim_name=="FadeOutAnimator": FadeOutAnimator(widget).start_()
		if anim_name=="FadeOutDownAnimator": FadeOutDownAnimator(widget).start_()
		if anim_name=="FadeOutLeftAnimator": FadeOutLeftAnimator(widget).start_()
		if anim_name=="FadeOutRightAnimator": FadeOutRightAnimator(widget).start_()
		if anim_name=="FadeOutUpAnimator": FadeOutUpAnimator(widget).start_()

		if anim_name=="RotateInAnimator": RotateInAnimator(widget).start_()
		if anim_name=="RotateInDownLeftAnimator": RotateInDownLeftAnimator(widget).start_()
		if anim_name=="RotateInDownRightAnimator": RotateInDownRightAnimator(widget).start_()
		if anim_name=="RotateInUpLeftAnimator": RotateInUpLeftAnimator(widget).start_()
		if anim_name=="RotateInUpRightAnimator": RotateInUpRightAnimator(widget).start_()

		if anim_name=="RotateOutAnimator": RotateOutAnimator(widget).start_()
		if anim_name=="RotateOutDownLeftAnimator": RotateOutDownLeftAnimator(widget).start_()
		if anim_name=="RotateOutDownRightAnimator": RotateOutDownRightAnimator(widget).start_()
		if anim_name=="RotateOutUpLeftAnimator": RotateOutUpLeftAnimator(widget).start_()
		if anim_name=="RotateOutUpRightAnimator": RotateOutUpRightAnimator(widget).start_()

		if anim_name=="SlideInDownAnimator": SlideInDownAnimator(widget).start_()
		if anim_name=="SlideInLeftAnimator": SlideInLeftAnimator(widget).start_()
		if anim_name=="SlideInRightAnimator": SlideInRightAnimator(widget).start_()
		if anim_name=="SlideInUpAnimator": SlideInUpAnimator(widget).start_()

		if anim_name=="SlideOutDownAnimator": SlideOutDownAnimator(widget).start_()
		if anim_name=="SlideOutLeftAnimator": SlideOutLeftAnimator(widget).start_()
		if anim_name=="SlideOutRightAnimator": SlideOutRightAnimator(widget).start_()
		if anim_name=="SlideOutUpAnimator": SlideOutUpAnimator(widget).start_()

		if anim_name=="ZoomInAnimator": ZoomInAnimator(widget).start_()
		if anim_name=="ZoomInDownAnimator": ZoomInDownAnimator(widget).start_()
		if anim_name=="ZoomInLeftAnimator": ZoomInLeftAnimator(widget).start_()
		if anim_name=="ZoomInRightAnimator": ZoomInRightAnimator(widget).start_()
		if anim_name=="ZoomInUpAnimator": ZoomInUpAnimator(widget).start_()

		if anim_name=="ZoomOutAnimator": ZoomOutAnimator(widget).start_()
		if anim_name=="ZoomOutDownAnimator": ZoomOutDownAnimator(widget).start_()
		if anim_name=="ZoomOutLeftAnimator": ZoomOutLeftAnimator(widget).start_()
		if anim_name=="ZoomOutRightAnimator": ZoomOutRightAnimator(widget).start_()
		if anim_name=="ZoomOutUpAnimator": ZoomOutUpAnimator(widget).start_()
		
		if anim_name=="FlyInAnimator": FlyInAnimator(widget).start_()
		if anim_name=="FlyOutAnimator": FlyOutAnimator(widget).start_()
		if anim_name=="DropOutAnimator": DropOutAnimator(widget).start_()
		if anim_name=="HingLeftAnimator": HingLeftAnimator(widget).start_()
		if anim_name=="HingRightAnimator": HingRightAnimator(widget).start_()
		if anim_name=="RollInAnimator": RollInAnimator(widget).start_()
		if anim_name=="RollOutAnimator": RollOutAnimator(widget).start_()


class AndroidViewAnimations(App):
	theme_cls= ThemeManager()
	theme_cls.primary_palette='Blue'

	def build(self):
		return Builder.load_string(kv)

if __name__ == '__main__':
	AndroidViewAnimations().run()