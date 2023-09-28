from pico2d import *


tuk_width, tuk_height = 1280, 1024
open_canvas(tuk_width, tuk_height)
player = load_image('character.png')
hand_arrow = load_image('hand_arrow.png')
tuk_Ground = load_image("TUK_GROUND.png")

index = 0
x, y = tuk_width  // 2, tuk_height // 2
running = True

def draw(frame):
    frameX, frameY, width, height = frame[index]
    player.clip_draw(frameX,frameY, width, height, x, y,100 , 150)

def player_run():
    global index
    frame = [(27,683-428,40,60), (71, 683-428,41,60), (123,683-428,38,60), 
    (173,683-428,33,60), (213,683-428,46,60), (261,683-428,41,60), 
    (312,683-428,38,60), (358,683-428,32,60)]
   	
    draw(frame)

    index += 1
    if(index == 8):
    	index = 0

def handle_events():
    global running
    events = get_events()
    for event in events:
    	if event.type == SDL_QUIT:
    		running = False
    	elif event.type == SDL_KEYDOWN:
    		running = False

while running:
    clear_canvas()
    tuk_Ground.draw(tuk_width//2,tuk_height//2)
    player_run()
    update_canvas()

    handle_events()
    delay(0.05)

    if not running: 
   	   break;