from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.animation import Animation

__all__ = ("WirelessRippleButton", "render")

render = """

<WirelessRippleButton>:

	ripple_rad0: 0
	ripple_alpha0: 0

	ripple_rad1: 0
	ripple_alpha1: 0

	ripple_rad2: 0
	ripple_alpha2: 0
	
	ripple_rad3: 0
	ripple_alpha3: 0

	ripple_rad4: 0
	ripple_alpha4: 0

	size_hint: None, None
	size: 50,50

	canvas.before:
		Color:
			rgba: self.ripple_color + [self.ripple_alpha0]
		Ellipse:
			size: self.ripple_rad0,self.ripple_rad0
			pos: self.x-(self.ripple_rad0/2-self.size[0]/2) ,self.y-(self.ripple_rad0/2-self.size[0]/2)
		
		Color:
			rgba: self.ripple_color + [self.ripple_alpha1]
		Ellipse:
			size: self.ripple_rad1,self.ripple_rad1
			pos: self.x-(self.ripple_rad1/2-self.size[0]/2) ,self.y-(self.ripple_rad1/2-self.size[0]/2)

		Color:
			rgba: self.ripple_color + [self.ripple_alpha2]
		Ellipse:
			size: self.ripple_rad2,self.ripple_rad2
			pos: self.x-(self.ripple_rad2/2-self.size[0]/2) ,self.y-(self.ripple_rad2/2-self.size[0]/2)

		Color:
			rgba: self.ripple_color + [self.ripple_alpha3]
		Ellipse:
			size: self.ripple_rad3,self.ripple_rad3
			pos: self.x-(self.ripple_rad3/2-self.size[0]/2) ,self.y-(self.ripple_rad3/2-self.size[0]/2)

		Color:
			rgba: self.ripple_color + [self.ripple_alpha4]
		Ellipse:
			size: self.ripple_rad4,self.ripple_rad4
			pos: self.x-(self.ripple_rad4/2-self.size[0]/2) ,self.y-(self.ripple_rad4/2-self.size[0]/2)
	
	canvas.after:
		Color:
			rgba: [1,1,1] + [1]
		Ellipse:
			source: "phone1.png"
			pos: self.x-((self.size[0]*1.5)/2-self.size[0]/2) ,self.y-((self.size[0]*1.5)/2-self.size[0]/2)
			size: self.size[0]*1.5, self.size[0]*1.5

	on_press:
		self.start_anim()
"""


class WirelessRippleButton(Button):

    ripple_color = [52 / 255, 152 / 255, 219 / 255]

    def __init__(
        self,
        max_rad=500,
        circle_count=5,
        duration=0.6,
        ripple_color=[52 / 255, 152 / 255, 219 / 255],
        **args
    ):
        self.max_rad = max_rad
        self.circle_count = circle_count if circle_count in range(1, 6) else 5
        self.duration = duration
        self.ripple_color = ripple_color
        self.but_size = self.size
        super(WirelessRippleButton, self).__init__(**args)

    def _initialize(self):
        """
		Function to reset atributes prior to animation
		"""
        for i in range(self.circle_count):
            setattr(self, "ripple_rad" + str(i), self.size[0] - 5)
            setattr(self, "ripple_alpha" + str(i), 1)

    def start_anim(self, *args):
        self._initialize()

        self.props = ["ripple_rad0", "ripple_alpha0"]
        self.vals = [
            self.max_rad / self.circle_count,
            (self.circle_count - 1) * 1 / self.circle_count,
        ]

        anim = Animation(d=self.duration, **dict(zip(self.props, self.vals)))

        self.anim_intermediate(anim)

    def anim_intermediate(self, anim):

        """
		A bit tricky part

		It takes(not really like as function arguments) props and vals for the first circle calculated 
		in `start_anim` and appends property name of subsequent circle to `props` list and shifts values of
		corresponding properties by one ripple circle by adding new values for first circle in the begining
		of `vals` list.

		Sort of like this:

			(new values)-->circle2---(values)---->circle1 and so on.
		"""
        for i in range(1, self.circle_count):
            self.props.extend(["ripple_rad" + str(i), "ripple_alpha" + str(i)])
            self.vals = [
                (i + 1) * self.max_rad / self.circle_count,
                (1 - (i + 1) / self.circle_count),
            ] + self.vals

            anim += Animation(d=self.duration, **dict(zip(self.props, self.vals)))
        anim.cancel_all(self)
        anim.bind(on_complete=self.anim_complete)
        anim.start(self)

    def anim_complete(self, obj, inst):

        ripple_rad_start = self.but_size[0] - 5
        ripple_alpha_start = 1

        props = []
        vals = []
        rads = []
        alphas = []

        """
		Working of property transfer from one ripple circle to another:

			|<----<----|
			0-->1---2-->
		"""

        for i in range(self.circle_count - 1, -1, -1):
            props.extend(["ripple_rad" + str(i), "ripple_alpha" + str(i)])
            rads.append("ripple_rad" + str(i))
            alphas.append("ripple_alpha" + str(i))

            if i == 0:
                vals.extend(
                    [
                        getattr(self, "ripple_rad" + str(self.circle_count - 1)),
                        getattr(self, "ripple_alpha" + str(self.circle_count - 1)),
                    ]
                )
            else:
                vals.extend(
                    [
                        getattr(self, "ripple_rad" + str(i - 1)),
                        getattr(self, "ripple_alpha" + str(i - 1)),
                    ]
                )

        # if radius becomes maximum, reset properties
        for rad, alpha in zip(rads, alphas):
            if getattr(self, rad) == self.max_rad:
                setattr(self, rad, ripple_rad_start)
                setattr(self, alpha, ripple_alpha_start)

        anim = Animation(d=self.duration, **dict(zip(props, vals)))
        anim.bind(on_complete=self.anim_complete)
        anim.start(self)


if __name__ == "__main__":
    WirelessRippleButton()
