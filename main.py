import pygame
import sys

pygame.init()

screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)

fps = 120
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 30, False, False)

pygame.display.set_caption("Game")
pygame.key.set_repeat(1)


class Object:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def object_display(self):
        pygame.draw.rect(screen, (0, 0, 255), [self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1], 0)


objects = []
objects.append(Object(0, 600, 700, 720))
objects.append(Object(200, 400, 600, 500))


class Player:
    speed_limit = 400
    speed_time = 0.05  #최고속도 도달 시간 second

    gravity = 10

    def __init__(self):
        self.size = [80, 80]
        self.pos = [0, 0]
        self.vel = [0, 0]
        self.accel = [0, 0]
        self.key_accel = [0, 0]
        self.collision_accel = [0,0]
        self.color = (0,0,0)
        self.text = 0
        self.on_ground = 0
        self.on_wall = 0
        self.ifcollision = 0

    def player_move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if self.vel[0] < Player.speed_limit and not self.on_wall == 1:
                    self.key_accel[0] = Player.speed_limit / Player.speed_time / fps
                else:
                    self.key_accel[0] = 0
            if event.key == pygame.K_a:
                if self.vel[0] > Player.speed_limit * (-1) and not self.on_wall == 2:
                    self.key_accel[0] = (-1) * Player.speed_limit / Player.speed_time / fps
                else:
                    self.key_accel[0] = 0
            '''
            if event.key == pygame.K_s:
                if self.vel[1] < Player.speed_limit:
                    self.key_accel[1] = Player.speed_limit / Player.speed_time / fps
                else:
                    self.key_accel[1] = 0
            '''
            if event.key == pygame.K_w:
                if self.vel[1] > Player.speed_limit * (-1) and self.on_ground == 1:
                    self.key_accel[1] = (-10) * Player.speed_limit / Player.speed_time / fps
                else:
                    self.key_accel[1] = 0
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

    def collision(self):
        pass





    def pos_update(self):
        self.accel[0] = self.key_accel[0]
        self.accel[1] = Player.gravity + self.key_accel[1] + self.collision_accel[1]

        self.vel[0] += self.accel[0]
        self.vel[1] += self.accel[1]

        self.pos[0] += self.vel[0] / fps
        self.pos[1] += self.vel[1] / fps

    def text_update(self):
        self.text = font.render(f'Pos: {list(map(int,self.pos))}, Vel:{self.vel}', True, (0, 0, 0))

    def player_display(self):
        pygame.draw.rect(screen, self.color, [self.pos[0], self.pos[1], self.size[0], self.size[1]], 0)

    def text_display(self):
        screen.blit(self.text, (200, 200))


James = Player()


def update():
    James.collision()
    James.pos_update()
    James.text_update()


def display():
    James.player_display()
    James.text_display()
    for i in objects:
        i.object_display()


while True:
    clock.tick(fps)
    screen.fill((255, 255, 255))
    update()
    display()
    for event in pygame.event.get():
        James.player_move()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
