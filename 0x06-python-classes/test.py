#!/usr/bin/env python3
class Robot:
    
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    def __getattr__(self, typee):
        return "nil"

robot = Robot("RoboBot", 2022, "TechCity")

print(robot.brp)
print(robot.__dict__)
print(robot.name)        
print(robot.build_year)  
print(robot.city)
