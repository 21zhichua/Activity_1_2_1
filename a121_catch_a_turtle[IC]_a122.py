# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
 
 
#-----game configuration----
spotColor = "pink"
spotShape = "circle"
spotSize = 5
score = 0
 
# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")
 
 
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
spot.speed(0)
score_writer = trtl.Turtle()
score_writer.pu()
score_writer.goto(-180,170)
spot.penup()
 
 
#-------Background color--------
wn=trtl.Screen()
wn.bgcolor("red")
 
 
# Game start
game_start = False
start = trtl.Turtle()
start.shape("triangle")
start.shapesize(5, 10, 0)
start.color("white")
def start_game(x, y):
  global game_start
  game_start = True
  start.hideturtle()
start.onclick(start_game)
while not(game_start):
  spot.hideturtle()
  spot.showturtle()
 
 
#add custom colors in the colors list
colors = ["yellow", "red", "green", "olive", "aquamarine", "orange", "purple", "pink", "medium purple", "seashell", "navy"]
def isosceles_triangle_clicked(x, y):
  global timer
  if timer_up == False:
    update_score()
    change_color()
    change_position()
def change_color():
  spot.color(rand.choice(colors))
  spot.stamp()
  spot.color("blue")
 
 
#-----game functions--------
def spot_clicked(x,y):
  size = rand.randint(1, 10)
  change_position(size)
  update_score()
def change_position(size):
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  colors = ["blue" , "red", "green", "pink", "black", "purple", "brown"]
  colorcycle = rand.randint(0,6)
  spot.hideturtle()
  spot.fillcolor(colors[colorcycle])
  spot.turtlesize(size)
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()
def update_score():
  global score
  score += 1
  print(score)
  score_writer.clear()
  score_writer.write(score, font=font_setup)
 
 
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
 
  global leader_scores_list
  global leader_names_list
  global score
  global spot
 
  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)
 
  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)
 
  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)
 
#-----events----------------
spot.onclick(spot_clicked)
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
 
 
#-----countdown writer-----
counter =  trtl.Turtle()
 
 
#-----game functions-----
counter.penup()
counter.goto(200, 200)
counter.pendown()
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
 
 
#---------events---------
wn = trtl.Screen()  
wn.ontimer(countdown, counter_interval)
 
 
 
wn = trtl.Screen()
wn.mainloop()

