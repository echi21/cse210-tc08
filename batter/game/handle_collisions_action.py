import sys

from game.action import Action
from game.point import Point
from game import constants


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game
    state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0]  # there's only one
        paddle = cast["paddle"][0]  # there's only one
        bricks = cast["brick"]
        # marquee.set_text("")

        """for brick in bricks:
            position = ball.get_position()
            if position.equals(brick.get_position()):
                brick.set_text(" ")
                x = position.get_x()
                y = position.get_y()
                x2 = 1
                y2 = 1
                x += x2
                y += y2
                new_position = Point(x, y)
                ball.set_position(new_position)
                ball.set_velocity(new_position)"""



        # I will have to type of collisions:
        # paddle and ball.
        # ball and bricks.



    #def _handle_escape_collision(self, cast):
        """Handles collisions. Stops the game
        if there is one.

        Args:
            self (Action): An instance of Action.
        """
        # Si la pelota toca el nivel de 'y' el juego termina

        """ball = cast["ball"][0]
        position = ball.get_position()

        x = position.get_x()
        y = position.get_y()

        if y == constants.MAX_Y:
            sys.exit()"""
