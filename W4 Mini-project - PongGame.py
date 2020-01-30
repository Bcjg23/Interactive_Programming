# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel=[0,0]
    ball_vel[1] = - random.randrange(60, 180)/60

    if direction == "RIGHT":
        ball_vel[0] = random.randrange(120, 240)/60
    elif direction == "LEFT":
        ball_vel[0] = - random.randrange(120, 240)/60
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = (HEIGHT - PAD_HEIGHT)/2
    paddle2_pos = (HEIGHT - PAD_HEIGHT)/2
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    score1 = 0
    score2 = 0
    
    #Call spawn_ball 
    spawn_ball("LEFT")
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of top and bottom sides of canvas
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT-BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
    # Determine whether paddle and ball collide or the ball and the gutter collide
    # determine if ball is near to the left extreme
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
        #If colides with paddle on the left
        if (ball_pos[1] >= paddle1_pos) and (ball_pos[1] <= (paddle1_pos+PAD_HEIGHT)):
            #Increase the velocity of the ball by 10% each time it strikes a paddle
            ball_vel[0] = -1.1* ball_vel[0] 
        else: #if colides with gutter on the rigth
            spawn_ball("RIGHT")
            #Update the score
            score2 += 1
    # determine if ball is near to the right extreme
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS): 
        #If colides with paddle on the left
        if ball_pos[1] >= (paddle2_pos) and ball_pos[1] <= (paddle2_pos+PAD_HEIGHT):
            ball_vel[0] =  -1.1*ball_vel[0]
        else: #if colides with gutter on the left
            spawn_ball("LEFT")
            #Update the score
            score1 += 1

    
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Red")
   
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos > 0 and paddle1_vel > 0) or (paddle1_pos < (HEIGHT - PAD_HEIGHT) and paddle1_vel < 0):
        paddle1_pos -= paddle1_vel
    
    if (paddle2_pos > 0 and paddle2_vel > 0) or (paddle2_pos < (HEIGHT - PAD_HEIGHT) and paddle2_vel < 0):
        paddle2_pos -= paddle2_vel
          
  
    # draw paddles
    canvas.draw_line([0, paddle1_pos],[0, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "BLUE")
    canvas.draw_line([WIDTH, paddle2_pos],[WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "FUCHSIA")
    
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/4, 50), 40, "White")
    canvas.draw_text(str(score2), (3*WIDTH/4, 50), 40, "White")

    
def button_handler():
    new_game()
    
            
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel_INC = 5
    #Velocity update for Paddle1
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = vel_INC
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = - vel_INC
        
    #Velocity update for Paddle2    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = vel_INC
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = - vel_INC

def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_vel_INC, paddle2_vel_INC
    
    #Velocity update for Paddle1
    if (key == simplegui.KEY_MAP["w"]) or (key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
        
    #Velocity update for Paddle2    
    if (key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        paddle2_vel = 0
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', button_handler)


# start frame
new_game()
frame.start()
