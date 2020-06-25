class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food

        self.snake = deque([(0,0)])
        self.eat = 0
    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        direct = {'U':(-1,0), 'L':(0,-1), 'R':(0,1), 'D':(1,0)}
        
        d = direct[direction]

        if 0 <= self.snake[0][0] + d[0] < self.height and 0 <= self.snake[0][1] + d[1] < self.width:

            if self.food and [self.snake[0][0] + d[0], self.snake[0][1] + d[1]] == self.food[0]:
                
                self.food.pop(0)
                self.snake.appendleft((self.snake[0][0] + d[0], self.snake[0][1] + d[1]))
                self.eat+=1
                return self.eat
            else:
        
                new_i = self.snake[0][0] + d[0]
                new_j = self.snake[0][1] + d[1]
                self.snake.pop()
                if (new_i, new_j) in self.snake:
                    return -1
                self.snake.appendleft((new_i,new_j ))       
            return self.eat
                
            
            
            
        else:
            return -1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)