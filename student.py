# class Student:
#     name="Elizabeth"
#     age=22
#     school="Akirachix"
#     nationality="Kenyan"
    
class Student:
    school="Akirachix"
    def __init__(self,first_name,age,nationality,last_name,country):
        self.first_name=first_name
        self.age=age
        self.nationality=nationality
        self.country=country
        self.last_name=last_name
        
    def greet_student(self):
            return (f"Hello {self.name} welcome to {Student.school}")
    def year_of_birth(self):
        year=2023-self.age
        return (f"Hello {self.name} you were born in {year}")
    def show_full_name(self):
        return(f"Hi my name is {self.first_name}  {self.last_name}")
    def show_initials(self):
        return(f"My initials are {self.first_name[0]}{self.last_name [0]}")
    

    
    