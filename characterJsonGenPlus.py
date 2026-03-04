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
  name = input("Enter your name: ").lowerCase().strip()
  age = int(input("Enter your age: ")).lowerCase().strip()
  skin_color = input("Enter your skin color: ").lowerCase().strip()
  eye_color = input("Enter your eye color: ").lowerCase().strip()
  hair_color = input("Enter your hair color: ").lowerCase().strip()
  hobbies = input("Enter your hobbies (separated by ', '): ").lowerCase().strip().split(", ")
  job = input("Enter your job: ").lowerCase().strip()
  gender = input("Enter your gender: ").lowerCase().strip()
  return person(name, age, skin_color, eye_color, hair_color, hobbies, job, gender)
# allow user to generate character and save it
char = user_person()
txt = path(char.name + ".json")
txt.write_text(json.dumps(char.__dict__, indent=1))
print(f"Your character was saved to '{char.name}.json'.")
