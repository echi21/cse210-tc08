from game.action import Action
from game.point import Point

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
        #bricks = cast["brick"]
        # marquee.set_text("")

        """for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                brick.set_text(" ")
                position = Point(1, 1)
                ball.set_position(position)"""

        """for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                text = artifact.get_text()
                marquee.set_text(text)"""

        # I will have to type of collisions:
        # paddle and ball.
        # ball and bricks.

        # def grow_tail(self):
        """Grows the snake's tail by one segment.

            Args:
                self (Snake): An instance of snake.
            """
        """tail = self._segments[-1]
            offset = tail.get_velocity().reverse()
            text = "#"
            position = tail.get_position().add(offset)
            velocity = tail.get_velocity()
            self._add_segment(text, position, velocity)"""





    def _handle_escape_collision(self):
        """Handles collisions between the snake's head and body. Stops the game
        if there is one.

        Args:
            self (Director): An instance of Director.
        """
        # Si la pelota toca el nivel de 'y' el juego termina
        head = self._snake.get_head()
        body = self._snake.get_body()
        for segment in body:
            if head.get_position().equals(segment.get_position()):
                self._keep_playing = False
                break
