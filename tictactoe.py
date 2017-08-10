import RPi.GPIO as GPIO, time, random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#LED grid vars; "c0" is column 1
c0 = [12, 29, 37]
c1 = [7, 18, 35]
c2 = [3, 15, 32]

#generate grid
grid = [c0, c1, c2]

#setup GPIO
GPIO.setup(c0, GPIO.OUT, initial=0)
GPIO.setup(c1, GPIO.OUT, initial=0)
GPIO.setup(c2, GPIO.OUT, initial=0)

#setup PWM objects in grid
for row in grid:
    for i in row:
        grid[grid.index(row)][row.index(i)] = GPIO.PWM(i, 50)

#lists to store moves made
played =[]
computer_moves = []
player_moves = []

#for setting the freq and duty cycle of player's and computer's 'pieces'
player_freq = 3
computer_freq = 50
computer_duty_cycle = 10

#game vars
playing_game = True
winner = None
players_turn = True

#coordinates for cursor
#LEDs referenced by coordinate plane, where (0,0) is lower left corner
curx = 0
cury = 0

#winning sequences, should be eight total
winning_sequences = [[grid[0][0], grid[1][0], grid[2][0]],
                    [grid[0][1], grid[1][1], grid[2][1]],
                    [grid[0][2], grid[1][2], grid[2][2]],
                    [grid[0][0], grid[0][1], grid[0][2]],
                    [grid[1][0], grid[1][1], grid[1][2]],
                    [grid[2][0], grid[2][1], grid[2][2]],
                    [grid[0][0], grid[1][1], grid[2][2]],
                    [grid[2][0], grid[1][1], grid[0][2]]]

#events for buttons
GPIO.add_event_detect(upb, GPIO.FALLING, bouncetime = 200)
GPIO.add_event_detect(downb, GPIO.FALLING, bouncetime = 200)
GPIO.add_event_detect(rightb, GPIO.FALLING, bouncetime=200)
GPIO.add_event_detect(leftb, GPIO.FALLING, bouncetime=200)
GPIO.add_event_detect(selectb, GPIO.FALLING, bouncetime=200)

#faulty func
def startLEDs(duty_cycle, freq):
    for row in grid:
        for i in row:
            i.start(duty_cycle)
            i.ChangeFrequency(freq)
            
#DELETE THIS FUNC
def flash(freq):    
    for row in grid:
        for i in row:
            i.stop()
            i.start(50)
            i.ChangeFrequency(freq)
        
    time.sleep(3)
    
    for row in grid:
        for i in row:
            i.ChangeDutyCycle(0)

def select():
    
    global curx
    global cury
    global players_turn
    
    if grid[curx][cury] not in played:
        grid[curx][cury].ChangeDutyCycle(50)
        grid[curx][cury].ChangeFrequency(player_freq)
        played.append(grid[curx][cury])
        player_moves.append(grid[curx][cury])
        players_turn = False
        speaker.ChangeFrequency(800)
        speaker.ChangeDutyCycle(50)
        time.sleep(0.25)
        speaker.ChangeDutyCycle(0)
        return players_turn
    
    else:
        players_turn = True
        speaker.ChangeFrequency(450)
        speaker.ChangeDutyCycle(50)
        time.sleep(0.25)
        speaker.ChangeDutyCycle(0)
        return players_turn

def up():
   
    global cury
    global curx
    
    if cury < 2:
        cury += 1
        grid[curx][cury].ChangeDutyCycle(100)
        grid[curx][cury].ChangeFrequency(50)
        if grid[curx][cury-1] in played:
            if grid[curx][cury-1] in player_moves:
                grid[curx][cury-1].ChangeDutyCycle(50)
                grid[curx][cury-1].ChangeFrequency(player_freq)
            if grid[curx][cury-1] in computer_moves:
                grid[curx][cury-1].ChangeDutyCycle(computer_duty_cycle)
                grid[curx][cury-1].ChangeFrequency(computer_freq)
        else:
            grid[curx][cury-1].ChangeDutyCycle(0)
        speaker.ChangeFrequency(650)
        speaker.ChangeDutyCycle(50)
        time.sleep(0.15)
        speaker.ChangeDutyCycle(0)
        
def down():

    global cury
    global curx
    
    if cury > 0:
        cury -= 1
        grid[curx][cury].ChangeDutyCycle(100)
        grid[curx][cury].ChangeFrequency(50)
        if grid[curx][cury+1] in played:
            if grid[curx][cury+1] in player_moves:
                grid[curx][cury+1].ChangeDutyCycle(50)
                grid[curx][cury+1].ChangeFrequency(player_freq)
            if grid[curx][cury+1] in computer_moves:
                grid[curx][cury+1].ChangeDutyCycle(computer_duty_cycle)
                grid[curx][cury+1].ChangeFrequency(computer_freq)
        else:
            grid[curx][cury+1].ChangeDutyCycle(0)
        speaker.ChangeFrequency(650)
        speaker.ChangeDutyCycle(50)
        time.sleep(0.15)
        speaker.ChangeDutyCycle(0)
           
def right():
    
    global cury
    global curx
    
    if curx < 2:
        curx += 1
        grid[curx][cury].ChangeDutyCycle(100)
        grid[curx][cury].ChangeFrequency(50)
        if grid[curx-1][cury] in played:
            if grid[curx-1][cury] in player_moves:
                grid[curx-1][cury].ChangeDutyCycle(50)
                grid[curx-1][cury].ChangeFrequency(player_freq)
            if grid[curx-1][cury] in computer_moves:
                grid[curx-1][cury].ChangeDutyCycle(computer_duty_cycle)
                grid[curx-1][cury].ChangeFrequency(computer_freq)
        else:
            grid[curx-1][cury].ChangeDutyCycle(0)
        speaker.ChangeFrequency(650)
        speaker.ChangeDutyCycle(50)
        time.sleep(0.15)
        speaker.ChangeDutyCycle(0)
        
def left():
   
    global cury
    global curx

    if curx > 0:
        curx -= 1
        grid[curx][cury].ChangeDutyCycle(100)
        grid[curx][cury].ChangeFrequency(50)
        if grid[curx+1][cury] in played:
            if grid[curx+1][cury] in player_moves:
                grid[curx+1][cury].ChangeDutyCycle(50)
                grid[curx+1][cury].ChangeFrequency(player_freq)
            if grid[curx+1][cury] in computer_moves:
                grid[curx+1][cury].ChangeDutyCycle(computer_duty_cycle)
                grid[curx+1][cury].ChangeFrequency(computer_freq)
        else:
            grid[curx+1][cury].ChangeDutyCycle(0)
        speaker.ChangeFrequency(650)
        speaker.ChangeDutyCycle(50)
        time.sleep(0.15)
        speaker.ChangeDutyCycle(0)
        
               
def checkForWin():
    
    global winning_sequences
    global computer_moves
    global player_moves
    
    check = 0
    
    for sequence in winning_sequences:
        for point in sequence:
            if point in computer_moves:
                check += 1
            else:
                break
            if check == 3:
                return 'computer'
        check = 0
        
    for sequence in winning_sequences:
        for point in sequence:
            if point in player_moves:
                check += 1
            else:
                break
            if check == 3:
                return 'player'
        check = 0

    if (len(player_moves) + len(computer_moves)) >= 9:
        return 'tie'
    
    return None
    


def computerMove():
    global players_turn

    #picked var is flag to indicate whether the computer has made a choice yet
    #choice is computer's move
    
    picked = False
    choice = None

    #if computer has two in a row, pick third one to win gamep
    if picked == False:
        for sequence in winning_sequences:
            current_points = []
            check = 0       
            for point in sequence:
                if point in computer_moves:
                    check += 1
                    current_points.append(point)
            if check == 2:
                for point in sequence:
                    if point not in current_points and point not in played:
                        choice = point
                        picked = True
                        break
                break
            
    #block player if player will win on next turn
    if picked == False:
        for sequence in winning_sequences:
            current_points = []
            check = 0
            for point in sequence:
                if point in player_moves:
                    check += 1
                    current_points.append(point)
            if check == 2:
                for point in sequence:
                    if point not in current_points and point not in played:
                        choice = point
                        picked = True
                        break
                break
            
    #pick center of grid if not already played
    if picked == False:
        if grid[1][1] not in played:
            choice = grid[1][1]
            picked = True
        else:
            picked = False
    
    #otherwise pick random point
    if picked == False:
        choice = grid[random.randint(0,2)][random.randint(0,2)]
        while choice in played:
            choice = grid[random.randint(0,2)][random.randint(0,2)]
        picked = True
        
    played.append(choice)
    computer_moves.append(choice)

    #computer's move is made, return that it's now the player's turn
    players_turn = True
    
    speaker.ChangeFrequency(65)
    speaker.ChangeDutyCycle(50)
    time.sleep(0.25)
    speaker.ChangeDutyCycle(0)

######---Start Buzzer Code---######

#frequencies of musical notes suitable to be played on buzzer
c = [32, 65, 131, 262]
db= [34, 69, 139, 277]
d = [36, 73, 147, 294]
eb= [37, 78, 156, 311]
e = [41, 82, 165, 330]
f = [43, 87, 175, 349]
gb= [46, 92, 185, 370]
g = [49, 98, 196, 392]
ab= [52, 104, 208, 415]
a = [55, 110, 220, 440]
bb= [58, 117, 223, 466]
b = [61, 123, 246, 492]

#this func plays a melody given a list of notes and beats
def playSong(songnotes, songbeats, tempo):
    speaker.ChangeDutyCycle(50)
    for i in range(0, len(songnotes)):
            speaker.ChangeFrequency(songnotes[i])
            time.sleep(songbeats[i]*tempo)
    speaker.ChangeDutyCycle(0)

#data list vars for melodies
loser_song_notes = [a[1], g[1], a[1], e[1], a[0]]
loser_song_beats = [1, 1, 2, 4, 4]
victory_song_notes = [g[2], g[1], g[2], d[3], b[2], d[3], g[3]]
victory_song_beats = [0.8, 0.2, 1, 2, 1, 1, 4]
tied_song_notes = [g[2], g[1], c[1], g[1], g[0], c[0]]
tied_song_beats = [1, 1, 1, 1, 1, 1, 2]

######---End Buzzer Code---######

try:
    #intro flash
    startLEDs(0, 1)
    startLEDs(50, 2)
    time.sleep(2)
    startLEDs(0, 2)
    
    while playing_game:
        
        while players_turn:
            if GPIO.event_detected(upb):
                up()
            if GPIO.event_detected(downb):
                down()
            if GPIO.event_detected(rightb):
                right()
            if GPIO.event_detected(leftb):
                left()
            if GPIO.event_detected(selectb):    
                select()
    
        if checkForWin() == 'player':
            winner = 'player'
            playing_game = False
            break

        if checkForWin() == 'tie':
            winner = 'tie'
            playing_game = False
            break

        time.sleep(1.25)
        computerMove()

        #see if anyone won    
        if checkForWin() == 'computer':
            
            for move in computer_moves:
                move.ChangeFrequency(computer_freq)
                move.stop()
                move.start(computer_duty_cycle)
            winner = 'computer'
            playing_game = False
            break

        if checkForWin() == 'tie':
            for move in computer_moves:
                move.ChangeFrequency(computer_freq)
                move.stop()
                move.start(computer_duty_cycle)
            winner = 'tie'
            playing_game = False
            break
            
        #display current moves
        for move in computer_moves:
            move.ChangeFrequency(computer_freq)
            move.stop()
            move.start(computer_duty_cycle)
            
        for move in player_moves:
            move.ChangeFrequency(player_freq)
            move.stop()
            move.start(50)
            
    #main game loop exited
            
    time.sleep(0.5)

    #display winning/losing animation and song
    
    if winner == 'player':
        startLEDs(0, 2)
        startLEDs(50, 2)
        playSong(victory_song_notes, victory_song_beats, 0.25)
        time.sleep(2)
        startLEDs(0, 1)
        
    if winner == 'computer':
        startLEDs(0, 2)
        startLEDs(50, 2)
        playSong(loser_song_notes, loser_song_beats, 0.25)
        time.sleep(3)
        startLEDs(0, 1)

    if winner == 'tie':
        startLEDs(0, 2)
        startLEDs(50, 2)
        playSong(tied_song_notes, tied_song_beats, 0.25)
        time.sleep(3)
        startLEDs(0, 1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
