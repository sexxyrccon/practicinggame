import pygame
import sys

pygame.init()

screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)

fps = 120
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 30, False, False)

pygame.display.set_caption("Game")


class Player:
    def __init__(self):
        self.size = [80, 80]
        self.pos = [0, 0]
        self.vel = [0, 0]
        self.accel = [0, 0]
        self.key_accel = [0, 0]
        self.speed_limit = 400
        self.text = font.render(f'X:{int(self.pos[0])}, Y:{int(self.pos[1])}', True, (0, 0, 0))

    def player_move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if self.vel[0] < self.speed_limit:
                    self.key_accel[0] = 1
            if event.key == pygame.K_a:
                if self.vel[0] > self.speed_limit * (-1):
                    self.key_accel[0] = -1
            if event.key == pygame.K_s:
                if self.vel[1] < self.speed_limit:
                    self.key_accel[1] = 1
            if event.key == pygame.K_w:
                if self.vel[1] > self.speed_limit * (-1):
                    self.key_accel[1] = -1
            if event.key == pygame.K_r:
                self.pos = [0, 0]
                self.vel = [0, 0]
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.key_accel[0] = 0
            if event.key == pygame.K_a:
                self.key_accel[0] = 0
            if event.key == pygame.K_s:
                self.key_accel[1] = 0
            if event.key == pygame.K_w:
                self.key_accel[1] = 0

    def pos_update(self):
        self.accel[0] = self.key_accel[0]
        self.accel[1] = self.key_accel[1]

        self.vel[0] += self.accel[0]
        self.vel[1] += self.accel[1]

        self.pos[0] += self.vel[0] / fps
        self.pos[1] += self.vel[1] / fps

    def text_update(self):
        self.text = font.render(f'X:{int(self.accel[0])}, Y:{int(self.accel[1])}', True, (0, 0, 0))

    def player_display(self):
        pygame.draw.rect(screen, (0, 0, 0), [self.pos[0], self.pos[1], self.size[0], self.size[1]], 0)

    def text_display(self):
        screen.blit(self.text, (200, 200))


James = Player()


def update():
    James.pos_update()
    James.text_update()


def display():
    James.player_display()
    James.text_display()


while True:
    clock.tick(fps)
    screen.fill((255, 255, 255))
    update()
    display()
    for event in pygame.event.get():
        James.player_move()
        print(James.key_accel)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
