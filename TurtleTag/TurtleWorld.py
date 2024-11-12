# TurtleWorld.py
import TurtleWorld 
from turtle import Turtle, Screen

class TurtleWorld:
    def __init__(self):
        self.window = Screen()
        self.turtles = []

    def setup_run(self):
        self.window.mainloop()

    def add_turtle(self, turtle):
        self.turtles.append(turtle)

    @property
    def animals(self):
        return self.turtles
