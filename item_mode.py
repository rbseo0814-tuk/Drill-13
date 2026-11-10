from pico2d import *

import game_framework


def init():
    pass


def finish():
    pass


def update():
    # 아이템 선택 중에는 게임 월드를 멈춰둔다.
    pass


def render():
    pass


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
