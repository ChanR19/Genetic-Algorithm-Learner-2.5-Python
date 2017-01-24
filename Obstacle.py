class Obstacle:
    x = 0
    y = 0
    w = 0
    
    def __init__(self,xPos,yPos,obstacleWidth):
        self.x = xPos
        self.y = yPos
        self.w = obstacleWidth
        
    def update(self):
        fill(105,105,105)
        ellipse(self.x,self.y,self.w,self.w);
