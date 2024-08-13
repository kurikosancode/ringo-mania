import pygame
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 120
FALLING_SPEED = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Object with Delta Time")


class FallingObject:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def update(self, dt):
        self.y += FALLING_SPEED * dt

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.size, self.size))

    def is_off_screen(self):
        return self.y > HEIGHT


def main():
    clock = pygame.time.Clock()
    running = True
    falling_object = FallingObject(WIDTH // 2, -50, 50)  # Start above the screen
    previous_time = time.time()

    while running:
        current_time = time.time()
        dt = current_time - previous_time
        previous_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        falling_object.update(dt)

        if falling_object.is_off_screen():
            print("The object is off the screen!")
            running = False

        screen.fill((0, 0, 0))
        falling_object.draw(screen)
        pygame.display.flip()

        print(clock.tick(FPS) / 100)

    pygame.quit()


if __name__ == "__main__":
    main()
