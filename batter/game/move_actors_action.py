from game import constants
from game.action import Action
from game.point import Point


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        for key in cast:
            if key == "paddle":
                paddle = cast[key]
                if not paddle[0].get_velocity().is_zero():
                    self._move_actor(paddle[0])

            elif key == "ball":
                ball = cast[key]
                self._move_actor(ball[0])

        # Bricks have zero velocity so, they don't call the move method.
        """for group in cast.values(): # Con values, lo que hace es recorrer individualmente el valor de cada key
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor) Original snippet"""

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its
        velocity. Will wrap the position from one side of the screen to the
        other when it reaches the edge in either direction.
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()

        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()

        x = x1 + x2
        y = y1 + y2

        position = Point(x, y)
        actor.set_position(position)
