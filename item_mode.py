from pico2d import *

import game_framework
import game_world

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def update():
    # 아이템 선택 중에는 게임 월드를 멈춰둔다.
    pass


def render():
    clear_canvas()
    # 멈춰있는 게임 화면 위에 아이템 선택 창을 띄운다.
    game_world.render()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 선택하지 않고 닫기
            game_framework.pop_mode()


def pause():
    pass


def resume():
    pass
