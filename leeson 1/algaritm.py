#линейний алгартим
#алгаритм с вветвлиями


class Point:

    def __init__(self,x,y):
        self.x= x
        self.y= y

    def get_max(self):
        if self.x < self.y:
            print(self.x)
        elif self.y > self.x:
            print(self.y)


    def replase_coord_values(self):
        tmp = self.y
        self.y = self.x
        self.x = tmp

int(input('введите знаечение x'))
int(input('введите знаечение y'))

poin1 = Point(x=1, y=5)





