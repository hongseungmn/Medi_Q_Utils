def sleep():print("클래스 외부(모듈의) 메소드:sleep()")
def eat():print("클래스 외부(모듈의) 메소드:eat()")

class Person:
  def __init__(self,name) -> None:
    self.name =name
  
  def sleep(self):print(self.name,'이(가) 자다',sep='')
  def eat(self):print(self.name,'이(가) 먹다',sep='')

  def print(self):
    sleep()
    eat()
    self.sleep()
    self.eat()

person = Person('가길동')
person.print()