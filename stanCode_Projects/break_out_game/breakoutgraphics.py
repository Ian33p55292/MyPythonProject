"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10   # Number of rows of bricks
BRICK_COLS = 10       # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

switch = True  # serve as the switch of deciding start the click_ball_move method or not
remove_brick_number = 0  # count the number of removed bricks


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(window_width-paddle_width)//2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius,
                            x=(window_width//2 - ball_radius), y=(window_height//2 - ball_radius))
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)  # when mouse moves --> def paddle_moves (Asynchronous)
        onmouseclicked(self.click_ball_move)  # when mouse click -->  def click_ball_move (Asynchronous)
        # Draw bricks
        brick_color_cols = 0
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height,
                                   x=j*(brick_width+brick_spacing), y=i*(brick_height+brick_spacing))
                self.brick.filled = True
                if brick_color_cols < 2:  # the columns of i=0 and i=1 are red bricks
                    self.brick.fill_color = 'red'
                elif 2 <= brick_color_cols < 4:
                    self.brick.fill_color = 'orange'
                elif 4 <= brick_color_cols < 6:
                    self.brick.fill_color = 'yellow'
                elif 6 <= brick_color_cols < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)
            brick_color_cols += 1

    def paddle_move(self, mouse):
        # important: mouse.x == self.paddle.x + self.paddle.width//2
        if mouse.x < self.paddle.width//2:   # when mouse.x < paddle.width/2 (that is, self.paddle.x < 0)
            self.paddle.x = 0  # self.paddle.x = left-top edge of the paddle, which must not exceed left window width
        elif mouse.x > (self.window.width - self.paddle.width//2):  # (that is, self.paddle.x > self.window.width - self.paddle.width)
            self.paddle.x = self.window.width - self.paddle.width  # which must not exceed right window width
        else:
            self.paddle.x = mouse.x - self.paddle.width//2

    def click_ball_move(self, mouse):
        global switch
        click_window = self.window.get_object_at(mouse.x, mouse.y)
        if click_window is None or click_window is self.ball or click_window is self.paddle or click_window is self.brick:  # detect the mouse click
            if self.__dx == 0 and self.__dy == 0 and switch:
                switch = False  # switch change to False -> call the ball_velocity method
                self.ball_velocity()

    def ball_velocity(self):
        global switch
        self.__dx = random.randint(1, MAX_X_SPEED)  # set x-direction velocity (self.__dx) randomly
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED  # set y-direction velocity (self.__dy)

    def set_x_y_boundary_check(self):
        if self.ball.x < 0 or self.ball.x > self.window.width:  # change direction of self.__dx if touch x-boundary
            self.__dx = -self.__dx
        if self.ball.y < 0:  # change direction of self.__dy if collide y-boundary (only top of the window)
            self.__dy = -self.__dy

    def y_exceed_window_height(self):
        global switch
        if self.ball.y > self.window.height:  # if collide the bottom of y-boundary -> lose game one time
            self.ball.x = self.window.width//2 - BALL_RADIUS   # reset ball to initial x-position
            self.ball.y = self.window.height//2 - BALL_RADIUS  # reset ball to initial y-position
            self.__dx = 0  # reset ball to zero velocity x
            self.__dy = 0  # reset ball to zero velocity x
            switch = True  # reopen the switch

    def get_dx(self):  # getter
        return self.__dx

    def get_dy(self):  # getter
        return self.__dy

    def detect_bounce(self):
        global remove_brick_number
        detect_1 = self.window.get_object_at(self.ball.x, self.ball.y)  # four detection points to detect collision
        detect_2 = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y)
        detect_3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS)
        detect_4 = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS)
        if detect_1 is not None:
            if detect_1 == self.paddle:  # if detection point 1 of ball collides on paddle
                if self.__dy > 0:  # only velocity of y-direction of ball is positive (downward) -> lead to ball bounce
                    # !!: this if statement prevent the ball up and down in the paddle
                    self.__dy = -self.__dy
            else:  # detection point 1 of ball collides on bricks
                self.window.remove(detect_1)  # remove bricks
                """
                !!: not remove self.brick, because the previous generated bricks are no longer self.brick.
                But the objects exist.
                detect_1, which is the brick object!
                """
                remove_brick_number += 1  # count the number of removed bricks
                self.__dy = -self.__dy
        elif detect_2 is not None:
            if detect_2 == self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            else:
                self.window.remove(detect_2)
                remove_brick_number += 1
                self.__dy = -self.__dy
        elif detect_3 is not None:
            if detect_3 == self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            else:
                self.window.remove(detect_3)
                remove_brick_number += 1
                self.__dy = -self.__dy
        elif detect_4 is not None:
            if detect_4 == self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            else:
                self.window.remove(detect_4)
                remove_brick_number += 1
                self.__dy = -self.__dy

    def clear(self):
        global remove_brick_number
        if remove_brick_number == BRICK_COLS*BRICK_ROWS:  # if all bricks are cleared -> game over
            self.ball.x = self.window.width // 2 - BALL_RADIUS  # reset ball to initial x-position
            self.ball.y = self.window.height // 2 - BALL_RADIUS  # reset ball to initial y-position
            self.__dx = 0  # reset ball to zero x-velocity
            self.__dy = 0  # reset ball to zero y-velocity


















