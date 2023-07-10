class Person:
  '''
  클래스 독 스트링
  사람 클래스입니다
  클래스 바로 밑에 위치 시킵니다
  '''
  def sleep(self):#인스턴스 메소드
    '''
    메소드 독 스트링
    sleep 메소드입니다
    '''
    print(self)
    print('자다')

  def eat(self):
    print('먹다')

person1 = Person()
print(f'value :{person1}, type :{type(person1)}, 주소 :{id(person1)}')
person1.sleep()
person1.eat()


person2 = Person()
print(f'value :{person2}, type :{type(person2)}, 주소 :{id(person2)}')
person2.sleep()
print(Person.__doc__)
print(person1.__doc__)
print(Person.sleep.__doc__)
print(Person.eat.__doc__)

class Person2(object):

  def __init__(self,name):
    self.name = name
    print('생성자')
  
  def sleep(self):
    print(self.name,'이(가) 자다',sep='')

  def eat(self):
    print(self.name,'이(가) 먹다',sep='')

person3 = Person2('홍길동')
person3.sleep()
person3.eat()
print(isinstance(person1,Person))