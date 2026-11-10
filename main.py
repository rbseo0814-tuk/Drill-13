from pico2d import*
from sdl2 import SDL_StopTextInput
import game_framework
import logo_mode

open_canvas()
# 한글 입력 상태에서는 IME가 알파벳 키(I, P 등)를 가로채 게임에 전달되지 않으므로
# 게임 창의 텍스트 입력(IME)을 끈다.
SDL_StopTextInput()
game_framework.run(logo_mode)
close_canvas()