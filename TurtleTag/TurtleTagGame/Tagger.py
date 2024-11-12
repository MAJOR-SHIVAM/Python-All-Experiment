# Tagger.py
from TurtleWorld import *
from Wobbler import *
import math

class Tagger(Wobbler):
    """A Tagger is a Wobbler that chases other Wobblers."""

    def __init__(self, world, speed=1, clumsiness=60, color='red'):
        super().__init__(world, speed, clumsiness, color)

    def steer(self):
        """Override to point toward the nearest neighbor."""
        closest_distance = float('inf')
        closest_turtle = None
        
        for turtle in self.world.animals:
            if turtle is not self:  # Skip itself
                distance = math.sqrt((self.x - turtle.x) ** 2 + (self.y - turtle.y) ** 2)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_turtle = turtle

        if closest_turtle is not None:
            # Calculate angle to the closest turtle
            angle_to_closest = math.atan2(closest_turtle.y - self.y, closest_turtle.x - self.x)
            angle_in_degrees = math.degrees(angle_to_closest)
            self.setheading(angle_in_degrees)  # Point towards the nearest turtle

        # Ensure the turtle stays within bounds
        if self.x < -200 or self.x > 200 or self.y < -200 or self.y > 200:
            self.rt(180)  # Turn around if out of bounds

def make_world(constructor):
    world = TurtleWorld()
    world.delay = 0.01
    world.setup_run()

    # Make three Taggers with different speed and clumsiness attributes
    colors = ['orange', 'green', 'purple']
    i = 1.0
    for color in colors:
        t = constructor(world, i, i * 30, color)
        i += 0.5

    return world

if __name__ == '__main__':
    world = make_world(Tagger)
    world.mainloop()
