from turtle import *
from Snake import Snake
from food import Food
from  score import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()


    # Detect  collision with wall
    if (snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280) :
        is_game_on=False
        scoreboard.game_over()


    # Detect collision with tail
for segment in snake.segment:
    if segment==snake.head:
        pass
    elif snake.head.distance(segment)<10:
# if head collides with any segment in the tail:
        game_is_on=False
#   trigger game_over
        scoreboard.game_over()


screen.exitonclick()















