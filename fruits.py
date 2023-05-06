class Fruits:
    category="fruits"
    def __init__(self,name,color,taste):
        self.name=name
        self.color=color
        self.taste=taste

    def type(self):
            return(f"This is a {self.name}")
    def shade(self):
            return(f"An {self.name} is {self.color} in color")
    def comparison(self):
            return(f"As compared to oranges {self.name} is {self.taste}")
        
Banana=Fruits(name="Banana",color="yellow",taste="sweet")
Oranges=Fruits(name="Oranges",color="orange",taste="sour")
print(Banana.comparison())
print(Oranges.shade())
print(Banana.type())
print(Banana.category)
        
    