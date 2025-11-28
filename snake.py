#GAME CONTROLS      // w-> up, s-> down, d-> right, a-> left //
print('/// 🍎WELCOME TO THE SNAKE GAME🐍 ///')
user_name:str = input('enter your User Name:')
print(f"{user_name}, you've entered the snake cage, also you are a snake..\n  you can move around and eat sweet apples")
print("by using: \nw(up) \ns(down) \nd(right) \na(left) \nand q(quit)")

#GAME SETUP
grid_size: int = 20
snake: list[list[int]] = [[10, 10], [9, 10], [8,10]]
apple_position: list[int] = [17, 17]
finish: bool = True
direction: list[int] = [0,0]
score: int = 0
#create game plan
while finish == True:
    for y in range(0,grid_size, 1):
        row: str = ''
        for x in range(0, grid_size, 1):
            if [x,y] == snake [0]:
                row = row + '🐍'
            elif [x,y] in snake:
                row = row + '🟩'
            elif [x,y] == apple_position:
                row = row + '🍎'
            elif x==19 or y==0 or y==19 or x==0:
                row = row + '🍃'
            else:
                row = row + '⬛'
        print(row)    

    print(score)

    user_input = input("press w(UP), a (LEFT), s(DOWN), d(RIGHT) or q(QUIT)")
    if user_input == 'w':
        direction = [0, -1]
    elif user_input == 's':
        direction = [0, 1]
    elif user_input == 'a':
        direction = [-1, 0]
    elif user_input == 'd':
        direction = [1, 0]
    elif user_input == 'q':
        print('GAME OVER')
        finish = False
    else:
        print('this is not a valid option')
    

    #calculate the new position of the head
    current_snake_head = snake[0]
    new_snake_head = [current_snake_head[0] + direction[0] , current_snake_head[1] + direction[1]]

    #move the snake  body with the new head
    if new_snake_head in snake or (new_snake_head[0]== 0 or new_snake_head[0]== grid_size - 1) or (new_snake_head[1]== 0 or new_snake_head[1]== grid_size - 1):
        print('GAME OVER')
        finish = False

    
    
    snake.insert(0, new_snake_head)

    if new_snake_head == apple_position:
        print('yayy! you ate the apple')
        score = score + 1
        import random
        apple_position = [random.randint(1, grid_size - 2), random.randint(1, grid_size - 2)]
    else:
        #remove the old
        snake.pop()
        continue


    print('git')
    
