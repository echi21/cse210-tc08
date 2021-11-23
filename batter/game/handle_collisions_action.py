import random
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

        self.handle_paddle_wall_collision(paddle)
        self.handle_ball_bricks_collision(bricks, ball)
        self.handle_ball_wall_collision(ball)
        self.handle_ball_paddle_collision(ball, paddle)
        self.handle_escape_collision(ball)

    # Collision methods for each case
    def handle_paddle_wall_collision(self, paddle):
        """Handles collisions between the paddle and the wall.
        If the paddle exceeds the limits, set it to a right position.
        Args:
            self (Action): An instance of Action.
            paddle (Actor): An instance of Actor.
        """

        position = paddle.get_position()

        x = position.get_x()
        y = position.get_y()

        if x >= 68:
            x = 68

        elif x <= 1:
            x = 1

        position = Point(x, y)
        paddle.set_position(position)

    def handle_ball_bricks_collision(self, bricks, ball):
        """Handles collisions between the ball and the bricks.
        If the ball hits the bricks, they turn empty strings.
        Args:
            self (Action): An instance of Action.
            bricks (Actor): An instance of Actor.
            ball (Actor): An instance of Actor.
        """
        ball_position = ball.get_position()
        ball_velocity = ball.get_velocity()
        dx = ball_velocity.get_x()
        dy = ball_velocity.get_y()
        for brick in bricks:
            text = brick.get_text()
            if ball_position.equals(brick.get_position()) and text == "*":
                brick.set_text(" ")
                dy *= -1  # Just change y axis because x axis is the same
                direction = Point(dx, dy)
                ball.set_velocity(direction)

    def handle_ball_wall_collision(self, ball):
        """Handles collisions between the ball and the wall.
        Keep the ball bouncing in the left, right and top sides.
        Args:
            self (Action): An instance of Action.
            ball (Actor): An instance of Actor.
        """
        position = ball.get_position()
        velocity = ball.get_velocity()

        x1 = position.get_x()  # 36
        y1 = position.get_y()  # 19
        x2 = velocity.get_x()  # 1
        y2 = velocity.get_y()  # -1

        # Agregue el =
        if x1 >= constants.MAX_X - 2 or x1 < 2:
            x2 *= -1

        if y1 > constants.MAX_Y - 1 or y1 < 1:
            y2 *= -1

        direction = Point(x2, y2)
        ball.set_velocity(direction)

    def handle_ball_paddle_collision(self, ball, paddle):
        """Handles collisions. Stops the game if there is one.
        Args:
            self (Action): An instance of Action.
            ball (Actor): An instance of Actor.
            paddle (Actor): An instance of Actor.
        """
        ball_position = ball.get_position()
        ball_velocity = ball.get_velocity()
        dx = ball_velocity.get_x()
        dy = ball_velocity.get_y()

        first_character = paddle.get_position()
        px = first_character.get_x()
        py = first_character.get_y()
        x_axis_characters_position = [px]

        for _ in range(10):
            px += 1
            x_axis_characters_position.append(px)

        for px in x_axis_characters_position:
            if ball_position.get_x() == px and ball_position.get_y() == py:
                dy *= -1
                # Quit the # symbol just in case you want to create a random
                # bouncing direction to increase the possibility of hitting all
                # the bricks. Yet, it needs to be perfectionated.
                # dx += random.randint(-1, 1)
                direction = Point(dx, dy)
                ball.set_velocity(direction)

    def handle_escape_collision(self, ball):
        """Handles collisions. Stops the game if there is one.
        Args:
            self (Action): An instance of Action.
            ball (Actor): An instance of Actor.
        """
        # Si la pelota toca el nivel de 'y' el juego termina
        position = ball.get_position()
        y = position.get_y()

        if y == constants.MAX_Y:
            sys.exit()
