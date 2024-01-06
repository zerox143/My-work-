import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH//2, HEIGHT//2)]
        self.direction = (1, 0)

    def move(self):
        head = self.body[-1]
        new_head = (head[0] + self.direction[0]*20, head[1] + self.direction[1]*20)
        self.body.append(new_head)
        self.body.pop(0)

    def grow(self):
        tail = self.body[0]
        new_tail = (tail[0] - self.direction[0]*20, tail[1] - self.direction[1]*20)
        self.body.insert(0, new_tail)

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(WINDOW, GREEN, (*segment, 20, 20))

# Food class
class Food:
    def __init__(self):
        self.position = (random.randrange(0, WIDTH, 20), random.randrange(0, HEIGHT, 20))

    def draw(self):
        pygame.draw.rect(WINDOW, RED, (*self.position, 20, 20))

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.direction = (1, 0)

        snake.move()

        if snake.body[-1] == food.position:
            snake.grow()
            food = Food()

        WINDOW.fill(WHITE)
        snake.draw()
        food.draw()
        pygame.display.update()

        clock.tick(10)

if __name__ == "__main__":
    main()
