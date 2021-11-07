

from game.action import Action


class DrawActorsAction(Action):

    def __init__(self, output_service):
        """The constructor should accept an argument called output_service (an instance of the OutputService class)
        and assign it to the corresponding attribute. """

        self._output_service = output_service

    """The execute method uses the output_service attribute to draw the actors on the screen.
    Be sure to clear the screen, draw the actors and then flush the buffer
    (see corresponding methods on the OutputService class)"""

    def execute(self, cast):
        self._output_service.clear_screen()
        
        for key in cast:
            actors = cast[key]
            self._output_service.draw_actors(actors)

        self._output_service.flush_buffer()
