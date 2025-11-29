from manim import *

# Animate a circle
class CreateCircle(Scene):
    def construct(self):
        circle = Circle() # Create a circle
        circle.set_fill(PINK, opacity=0.5) # set the color and transparency
        self.play(Create(circle)) # show the circle on the screen

# Transforming a square into a circle
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI/4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

# TODO: Next Positioning Mobject S