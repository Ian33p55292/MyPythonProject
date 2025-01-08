"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    # Add the animation loop here!
    live = 0
    graphics = BreakoutGraphics()
    while True:
        dx = graphics.get_dx()   # before click, the dx, dy are 0 --> stay in this while loop until detect click
        dy = graphics.get_dy()
        if dx != 0 and dy != 0:
            break  # leave this while loop
        pause(FRAME_RATE)
    while live < NUM_LIVES:  # the number of lives (the numbers that the user can attempt)
        graphics.ball.move(dx, dy)
        graphics.detect_bounce()  # detect the bouncing condition
        graphics.set_x_y_boundary_check()  # ball not exceeds the boundary of window width
        if graphics.ball.y > graphics.window.height:  # ball fall below the bottom of window
            graphics.y_exceed_window_height()  # reset the game
            live += 1  # lose one attempt
        graphics.clear()  # determine whether all the bricks are cleared
        dx = graphics.get_dx()  # get x-velocity: dx in user side
        dy = graphics.get_dy()
        pause(FRAME_RATE)






if __name__ == '__main__':
    main()
