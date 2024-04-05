# class
class CAR:
    def __init__(self, brand=str, model=str, year=int, color=str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
    def sound(self):
        return 'zooommm!!!!'
    
motor = CAR('Honda', 'Accord', '2013', 'White')
print(motor.sound())
        
class AC:
    def __init__(self, brand, model, horsepower, color):
        self.brand = brand
        self.model = model
        self.horsepower = horsepower
        self.color = color
        
    def cold(self):
        return 'weather'

aircon = AC('lg', 'v2', '50', 'yyellow')
print(aircon.cold())   
      