class Organism:
    x = 0
    y = 0
    w = 0
    hit = False
    hit_target_num = 0
    hit_target = False
    hit_target_counted = False
    tag = 0
    organismDNA = []
    fitness = 0
    timer = 0
    sequence = 0
    
    def __init__(self,xPos,yPos,organismWidth,generalDNA):
        self.x = xPos
        self.y = yPos
        self.w = organismWidth
        self.organismDNA = generalDNA
        
    def update(self):  
        global x,y,timer,sequence,hit_target_num,hit_target
        if self.hit != True:                
            self.x += self.organismDNA[self.sequence][0]
            self.y += self.organismDNA[self.sequence][1]
            if self.timer > self.organismDNA[self.sequence][2]:
                self.sequence += 1
                self.timer = 0 
            if self.sequence >= len(self.organismDNA):
                self.sequence = 0
            self.timer+=1
        if self.hit_target_num == 1:
            self.hit_target = True
        fill(0)
        ellipse(self.x,self.y,self.w,self.w);
    
    def mutate(self,mutationRate,durationMultiple):
        for i in range(len(self.organismDNA)):
            for j in range(2):
                if random(0,1) < 0.5:
                    self.organismDNA[i][j] += random(0,mutationRate) * -1
                else:
                    self.organismDNA[i][j] += random(0,mutationRate)
            if random(0,1) < 0.5 and self.organismDNA[i][2] > durationMultiple:
                self.organismDNA[i][2] += random(0,mutationRate) * -1 * durationMultiple
            else:
                self.organismDNA[i][2] += random(0,mutationRate)* durationMultiple
