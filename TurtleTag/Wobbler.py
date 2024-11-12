import turtle
from random import randint

class Wobbler(turtle.Turtle):
    """A Wobbler is a kind of Turtle with attributes for speed and clumsiness."""

    def __init__(self, speed=1, clumsiness=60, color='red'):
        super().__init__()  # Initialize the Turtle
        self.speed(0)  # Fastest speed
        self.clumsiness = clumsiness
        self.color(color)

        # Move to the starting position
        self.penup() 
        self.right(randint(0, 360))
        self.backward(150)

    def step(self):
        """Step is called to move the Wobbler."""
        self.steer()
        self.wobble()
        self.move()

    def move(self):
        """Move forward in proportion to self.speed."""
        self.forward(10)  # Move forward by a fixed amount

    def wobble(self):
        """Make a random turn in proportion to self.clumsiness."""
        direction = randint(-self.clumsiness, self.clumsiness)
        self.right(direction)

    def steer(self):
        """Steer the Wobbler in the general direction it should go."""
        self.right(10)  # Turn slightly to the right

def make_world():
    # Create Wobblers with different speed and clumsiness attributes
    colors = ['orange', 'green', 'purple']
    for i, color in enumerate(colors, start=1):
        Wobbler(speed=i, clumsiness=i * 10, color=color)

def main():
    # Set up the turtle environment
    turtle.bgcolor("lightblue")
    turtle.title("Wobbler Turtles")
    
    # Create Wobblers
    make_world()
    
    # Main loop to update the Wobblers
    while True:
        for wobbler in turtle.turtles():
            wobbler.step()  # Call the step method for each wobbler
        turtle.update()  # Update the screen

if __name__ == '__main__':
    main()
