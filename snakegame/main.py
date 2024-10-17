from turtle import Screen, Turtle, Shape
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import  time

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)#to turn off turtle animation
#tracer is connected to screen update to show the updates when we want

snake = Snake()
food = Food()
scoreboard = Scoreboard()


#CONTROL USING KEYS
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()  # to view the snake pattern
    time.sleep(0.1)  # good to visualize what is happening  and to refresh the screen
    snake.move()

    #detect collision of snake with food
    #using distance method
    if snake.head.distance(food) < 15: #distnace of the head of the snake to the food
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    #after the snake has collided with food, then it should go to a random new place - a method in food class

    #DETECT COLLISION WITH WALL
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor()<-280):
        scoreboard.reset()
        snake.reset()

    #DETECT COLLISION WITH TAIL
    # IF HEAD COLLIDES WITH ANY SEGMENT OF THE SNAKE BODY
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10: #edge case : snake.head.distance(head)
            scoreboard.reset()
            snake.reset()



screen.exitonclick()