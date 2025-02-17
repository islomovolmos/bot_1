from turtle import screensize, Screen,Turtle
# from zipfile import sizeEndCentDir


from snake import Snake
from food import Food
from score import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('snake Game')
screen.tracer(0)
screen.listen()


snake=Snake()
food=Food()
score=Scoreboard()
# ilonni harakatlantirish
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_is_on=True



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        score.abb_score()
        snake.extend_snake()

    if snake.segments[0].xcor()>299 or snake.segments[0].ycor()>299 or snake.segments[0].ycor()<-299:
         game_is_on=False
         score.game_over()



screen.exitonclick()