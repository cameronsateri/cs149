"""Simple bouncing ball simulation in pygame.

Author: CS 149 Instructors and Cameron Sateri
Version: 12/1/22

"""
import pygame

GRAVITY = 1.0
SCREEN_SIZE = (720, 480)
RED = (255, 0, 0)

class BounceGame:
    """This class handles the user interaction and the main game loop."""

    def __init__(self):
        """Initialize necessary pygame variables."""
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.fps = 60  # Frames per second.
        self.sprites = []  # The objects that will appear on the screen.

    def add_sprite(self, sprite):
        """Add a sprite to the sprite list."""
        self.sprites.append(sprite)

    def load_game(self, file_name):
        """Load a collection of balls from a file."""
        # UNFINISHED
        # Open the file to read
        # You may use a loop to run through the file, and use .split() method add the values to a dictonary for efficient individual access
        with open(file_name) as balls:
            balls.
        pass

    def save_game(self, file_name):
        """Save the current collection of balls to a file."""
        # UNFINISHED
        pass

    def run(self):
        """Execute the main game loop."""
        while True:
            self.clock.tick(self.fps)

            for event in pygame.event.get(): # Check for user input.
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        print("SAVE THE FILE!")

            self.screen.fill((0, 0, 0))  # Black out the screen

            for ball in self.sprites:
                ball.update()
                ball.draw()

            pygame.display.update()



class Ball:
    """A bouncy ball."""

    def __init__(self, x, y, radius, color, screen):
        """Initialize a ball at a particular location."""
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen
        self.vel_x = 0.0
        self.vel_y = 0.0

    def update(self):
        """Move the ball according to current velocity and gravity."""
        self.vel_y += GRAVITY
        self.x += self.vel_x
        self.y += self.vel_y
        width, height = self.screen.get_size()
        if self.y > height:
            self.y = height
            self.vel_y = -abs(self.vel_y)

    def draw(self):
        """Draw the ball to the screen."""
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)),
                           self.radius)

def main():
    """Run the application."""
    game = BounceGame()

    # You may want to use loop to pass different arguments (received from game.load_game) to call game.add_sprite method
    # This will be replaced with a call to game.load_game
    game.add_sprite(Ball(360, 50, 20, RED, game.screen))

    game.run()


if __name__ == "__main__":
    main()
