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

import sys

sys.path.append("../")

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


kv = """
#import MDToolbar kivymd.toolbar.MDToolbar
#:import C kivy.utils.get_color_from_hex
#import MDList kivymd.list.MDList
#import OneLineListItem kivymd.list.OneLineListItem

<ListItem@OneLineListItem>:
	theme_text_color: 'Custom'
	text_color: [1,1,1,1]
	bold: True
	on_release:
		app.root.animate(app.root.ids.lbl_parent, self.text)

MyLabel:
	orientation: "vertical"
	
	FloatLayout:
		size_hint_y: .4

		AnchorLayout:
			id: lbl_parent
			pos_hint: {"center_x":0.5, "center_y": 0.5}
			size_hint: None, None
			size: self.parent.width/2, self.parent.height/2

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
			ListItem:
				text:"PulseAnimator"
			ListItem:
				text:"RubberBandAnimator"
			ListItem:
				text:"ShakeAnimator"
			ListItem:
				text:"SwingAnimator"
			ListItem:
				text:"WobbleAnimator"
			ListItem:
				text:"TadaAnimator"
			ListItem:
				text:"WaveAnimator"

			ListItem:
				text:"BounceInAnimator"
			ListItem:
				text:"BounceInDownAnimator"
			ListItem:
				text:"BounceInLeftAnimator"
			ListItem:
				text:"BounceInRightAnimator"
			ListItem:
				text:"BounceInUpAnimator"

			ListItem:
				text:"FadeInAnimator"
			ListItem:
				text:"FadeInDownAnimator"
			ListItem:
				text:"FadeInLeftAnimator"
			ListItem:
				text:"FadeInRightAnimator"
			ListItem:
				text:"FadeInUpAnimator"

			ListItem:
				text:"FadeOutAnimator"
			ListItem:
				text:"FadeOutDownAnimator"
			ListItem:
				text:"FadeOutLeftAnimator"
			ListItem:
				text:"FadeOutRightAnimator"
			ListItem:
				text:"FadeOutUpAnimator"

			ListItem:
				text:"RotateInAnimator"
			ListItem:
				text:"RotateInDownLeftAnimator"
			ListItem:
				text:"RotateInDownRightAnimator"
			ListItem:
				text:"RotateInUpLeftAnimator"
			ListItem:
				text:"RotateInUpRightAnimator"

			ListItem:
				text:"RotateOutAnimator"
			ListItem:
				text:"RotateOutDownLeftAnimator"
			ListItem:
				text:"RotateOutDownRightAnimator"
			ListItem:
				text:"RotateOutUpLeftAnimator"
			ListItem:
				text:"RotateOutUpRightAnimator"

			ListItem:
				text:"SlideInDownAnimator"
			ListItem:
				text:"SlideInLeftAnimator"
			ListItem:
				text:"SlideInRightAnimator"
			ListItem:
				text:"SlideInUpAnimator"

			ListItem:
				text:"SlideOutDownAnimator"
			ListItem:
				text:"SlideOutLeftAnimator"
			ListItem:
				text:"SlideOutRightAnimator"
			ListItem:
				text:"SlideOutUpAnimator"
	
			ListItem:
				text:"ZoomInAnimator"
			ListItem:
				text:"ZoomInDownAnimator"
			ListItem:
				text:"ZoomInLeftAnimator"
			ListItem:
				text:"ZoomInRightAnimator"
			ListItem:
				text:"ZoomInUpAnimator"

			ListItem:
				text:"ZoomOutAnimator"
			ListItem:
				text:"ZoomOutDownAnimator"
			ListItem:
				text:"ZoomOutLeftAnimator"
			ListItem:
				text:"ZoomOutRightAnimator"
			ListItem:
				text:"ZoomOutUpAnimator"

			ListItem:
				text:"FlyInAnimator"
			ListItem:
				text:"FlyOutAnimator"
			ListItem:
				text:"DropOutAnimator"
			ListItem:
				text:"HingLeftAnimator"
			ListItem:
				text:"HingRightAnimator"
			ListItem:
				text:"RollInAnimator"
			ListItem:
				text:"RollOutAnimator"
		
"""


class MyLabel(BoxLayout):
    defaults = {
        "pos_hint": {"center_x": 0.5, "center_y": 0.5},
        "size": "",
        "opacity": 1,
        "angle": 0,
        "origin_": "",
    }

    def reset(self, widget):
        for key, val in self.defaults.items():
            if key == "size":
                val = (widget.parent.width / 2, widget.parent.height / 2)
            setattr(widget, key, val)

    def animate(self, widget, anim_name):
        self.reset(widget)
        try:
            eval(anim_name)(widget).start_()
        except NameError:
            pass


class AnimatorDemo(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "Blue"

    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
    AnimatorDemo().run()
