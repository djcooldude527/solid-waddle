# modules
from pathlib import Path as path
import json
# person class
class person:
  def __init__(self, name, age, skin_color, eye_color, hair_color, hobbies, job, gender):
    self.name = name
    self.age = age
    self.skin_color = skin_color
    self.eye_color = eye_color
    self.hair_color = hair_color
    self.hobbies = hobbies
    self.job = job
    self.gender = gender
# user-generated person
def user_person():
  name = input("Enter your name: ")
  age = int(input("Enter your age: "))
  skin_color = input("Enter your skin color: ")
  eye_color = input("Enter your eye color: ")
  hair_color = input("Enter your hair color: ")
  hobbies = input("Enter your hobbies (separated by ', '): ").split(", ")
  job = input("Enter your job: ")
  gender = input("Enter your gender: ")
  return person(name, age, skin_color, eye_color, hair_color, hobbies, job, gender)
# allow user to generate character and save it
char = user_person()
txt = path(char.name + ".json")
txt.write_text(json.dumps(char.__dict__, indent=1))
print(f"Your character was saved to '{char.name}.json'.")