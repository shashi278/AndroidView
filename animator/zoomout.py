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
from functools import partial

from .base import Animator

__all__ = (
    "ZoomOutAnimator",
    "ZoomOutDownAnimator",
    "ZoomOutLeftAnimator",
    "ZoomOutRightAnimator",
    "ZoomOutUpAnimator",
)


class ZoomOutAnimator(Animator):
    def start_(self, tmp=None):
        props = ["height", "width", "opacity"]

        vals = [self._original["height"] * 0, self._original["width"] * 0, 0]
        anim = Animation(d=self.duration, **dict(zip(props, vals)))

        self._animate(anim)


class ZoomOutDownAnimator(Animator):
    def start_(self, tmp=None):
        props = ["height", "width", "opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val + 0.05
            else:
                __tmp[key] = val
        vals = [
            self._original["height"] * 0.45,
            self._original["width"] * 0.45,
            1,
            __tmp,
        ]
        anim = Animation(d=self.duration / 2, **dict(zip(props, vals)))

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = -0.2
            else:
                __tmp[key] = val
        vals = [self._original["height"] * 0.1, self._original["width"] * 0.1, 0, __tmp]
        anim += Animation(d=self.duration / 2, **dict(zip(props, vals)))

        self._animate(anim)


class ZoomOutLeftAnimator(Animator):
    def start_(self, tmp=None):
        props = ["height", "width", "opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val - 0.05
            else:
                __tmp[key] = val
        vals = [
            self._original["height"] * 0.45,
            self._original["width"] * 0.45,
            1,
            __tmp,
        ]
        anim = Animation(d=self.duration / 2, **dict(zip(props, vals)))

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = -0.2
            else:
                __tmp[key] = val
        vals = [self._original["height"] * 0.1, self._original["width"] * 0.1, 0, __tmp]
        anim += Animation(d=self.duration / 2, **dict(zip(props, vals)))

        self._animate(anim)


class ZoomOutRightAnimator(Animator):
    def start_(self, tmp=None):
        props = ["height", "width", "opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = val + 0.05
            else:
                __tmp[key] = val
        vals = [
            self._original["height"] * 0.45,
            self._original["width"] * 0.45,
            1,
            __tmp,
        ]
        anim = Animation(d=self.duration / 2, **dict(zip(props, vals)))

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_x", "x", "left"]:
                __tmp[key] = 1.2
            else:
                __tmp[key] = val
        vals = [self._original["height"] * 0.1, self._original["width"] * 0.1, 0, __tmp]
        anim += Animation(d=self.duration / 2, **dict(zip(props, vals)))

        self._animate(anim)


class ZoomOutUpAnimator(Animator):
    def start_(self, tmp=None):
        props = ["height", "width", "opacity", "pos_hint"]

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = val - 0.05
            else:
                __tmp[key] = val
        vals = [
            self._original["height"] * 0.45,
            self._original["width"] * 0.45,
            1,
            __tmp,
        ]
        anim = Animation(d=self.duration / 2, **dict(zip(props, vals)))

        __tmp = {}
        for key, val in self._original["pos_hint"].items():
            if key in ["center_y", "y", "top"]:
                __tmp[key] = 1.2
            else:
                __tmp[key] = val
        vals = [self._original["height"] * 0.1, self._original["width"] * 0.1, 0, __tmp]
        anim += Animation(d=self.duration / 2, **dict(zip(props, vals)))

        self._animate(anim)
