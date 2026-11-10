from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    images = {}  # 크기별 이미지를 한 번만 로드해서 공유

    def __init__(self, x, y, velocity):
        if 'small' not in Ball.images:
            Ball.images['small'] = load_image('ball21x21.png')
        self.image = Ball.images['small']
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
