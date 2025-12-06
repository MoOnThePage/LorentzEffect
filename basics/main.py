from manim import *
from poetry.console.commands import self
from typing_extensions import runtime


# Animate a circle
class CreateCircle(Scene):
    def construct(self):
        circle = Circle() # Create a circle
        circle.set_fill(PINK, opacity = 0.5) # set the color and transparency
        self.play(Create(circle)) # show the circle on the screen

# Transforming a square into a circle
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)

        square = Square()
        square.rotate(PI/4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

# Positioning Mobjects
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(RED_A, opacity = 0.5) # set color and transparency

        square = Square() # create a sqaure
        square.set_fill(WHITE, opacity = 0.5)

        square.next_to(circle, DOWN, buff = 0.5) # set the positions
        self.play(Create(circle), Create(square)) # show the shapes on screen

# Using .animate syntax to animate methods
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square().set_fill(GREEN, opacity = 0.5)

        self.play(Create(square)) # Show the square
        self.play(square.animate.rotate(PI / 4)) # Rotate the square
        self.play(Transform(square, circle)) # Transform the square into circle
        self.play(square.animate.set_fill(PINK, opacity = 0.5)) # color the circle on the screen

class DifferentRotation(Scene):
    def construct(self):
        left_square = Square(color = YELLOW, fill_opacity = 0.7).shift(2 * LEFT)
        right_square = Square(color = RED, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(left_square.animate.rotate(PI), Rotate(right_square, angle = PI), runtime = 2)
        self.wait()

# Transform vs ReplacementTransform
class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()

class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a,t))