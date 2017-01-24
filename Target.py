class Target:
    x = 0
    y = 0
    w = 0
    
    def __init__(self,xPos,yPos,targetWidth):
        self.x = xPos
        self.y = yPos
        self.w = targetWidth
        
    def update(self):
        fill(255,0,0);
        ellipse(self.x, self.y, self.w,self.w);
        fill(255,255,255);
        ellipse(self.x, self.y, self.w - 10,self.w - 10);
        fill(255,0,0);
        ellipse(self.x, self.y, self.w - 20,self.w - 20);
