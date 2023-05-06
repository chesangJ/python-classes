class Car:
    make="BMW"
    def __init__(self,model,color,mileage):
        self.model=model
        self.color=color
        self.mileage=mileage
        
    def buying(self):
            return(f"{self.model} has been bought")
        
    def start(self):
            return(f"A {self.color} {self.model} has started ")
        
    def speed(self):
            mileage=(13*100)/500
            return(f"{self.model} has a {self.mileage} of {mileage}")

Bmw1=Car(model="5x series",color="blue",mileage="mileage")
Bmw2=Car(model="x5",color="white",mileage="mileage")  
print(Bmw1.buying())
print(Bmw2.speed())
print(Bmw2.make)





























       
        
     
        