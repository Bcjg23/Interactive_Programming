# template for "Stopwatch: The Game"


import simplegui

# define global variables
INTERVAL = 100 #0.1 seconds
WIDTH = 200
HEIGHT = 200
counter = 0
total_clicks = 0
clicks_on_target = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t//(60*10)
    tenthsSecs = t % 10
    seconds = (t//10) % 60
    
    #Update minutes if the seconds is greater than 59
    if seconds > 59: 
            seconds = seconds - 60
            minutes = minutes + 1
            
    #Print in any case
    if minutes == 0 and seconds == 0:
        return "0:00." + str(tenthsSecs)
    elif minutes == 0:
        if seconds < 10:
            return "0:0" + str(seconds) + "." + str(tenthsSecs)
        else:
            return "0:" + str(seconds) + "." + str(tenthsSecs)
    else:
        if seconds < 10:
            return str(minutes) + ":0" + str(seconds) + "." + str(tenthsSecs)
        else:
            return str(minutes) + ":" + str(seconds) + "." + str(tenthsSecs)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
# Event handlers for buttons 
def start_timer():
    timer.start()

def stop_timer():
    #Update the number of clicks
    global total_clicks, clicks_on_target
    total_clicks +=1
    #Update if you click on a whole second
    if (counter % 10) == 0:
        clicks_on_target += 1
    #Stops the timer
    timer.stop()

def reset_timer():
    global counter, total_clicks, clicks_on_target
    counter = 0
    total_clicks = 0
    clicks_on_target = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    #print counter
    counter += 1
    
# define draw handler
def draw(canvas):
    global total_clicks, clicks_on_target
    if counter < 6000:
        # Prints the watch on the canvas
        t_format = format(counter)
        canvas.draw_text(str(t_format), (WIDTH/2, HEIGHT/2), 18, 'Orange')
        # Prints the score of the player
        text = str(clicks_on_target) + "/" + str(total_clicks)
        canvas.draw_text(text, (160, 20), 18, 'Orange')
    else:
        stop_timer()
        reset_timer()
    
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", WIDTH, HEIGHT)
timer = simplegui.create_timer(INTERVAL, tick)

# Register event handlers
frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", reset_timer, 100)
frame.set_draw_handler(draw)


# Start timer
#timer.start()
frame.start()


# Please remember to review the grading rubric
