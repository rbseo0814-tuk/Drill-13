import os

from pico2d import *
import pico2d.pico2d as pico2d_core  # renderer, 데이터 폴더 경로 접근용
from sdl2 import SDL_BLENDMODE_BLEND, SDL_SetRenderDrawBlendMode

import game_framework
import game_world
import title_mode

font = None
small_font = None


def init():
    global font, small_font
    # pico2d 패키지에 들어있는 한글 지원 폰트 사용
    font_path = os.path.join(os.path.dirname(pico2d_core.__file__), 'data', 'ConsolaMalgun.ttf')
    font = load_font(font_path, 48)
    small_font = load_font(font_path, 22)


def finish():
    global font, small_font
    font = None
    small_font = None


def update():
    # 일시정지 중에는 게임 월드를 업데이트하지 않는다.
    pass


def render():
    clear_canvas()
    # 멈춰있는 게임 화면을 그대로 그리고, 그 위에 반투명 막을 덮는다.
    game_world.render()
    SDL_SetRenderDrawBlendMode(pico2d_core.renderer, SDL_BLENDMODE_BLEND)
    draw_rectangle(0, 0, get_canvas_width(), get_canvas_height(), 0, 0, 0, 150, filled=True)
    draw_rectangle(250, 200, 550, 400, 230, 230, 230, 255, filled=True)

    font.draw(310, 340, 'PAUSED', (40, 40, 40))
    small_font.draw(290, 270, 'P : 계속하기', (60, 60, 60))
    small_font.draw(290, 235, 'ESC : 타이틀로', (60, 60, 60))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            game_framework.change_mode(title_mode)


def pause():
    pass


def resume():
    pass
