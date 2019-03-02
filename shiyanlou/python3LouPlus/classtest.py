#!/usr/bin/env python3

class UserData:
    def __init__(self,id,name):
        self.id=id
        self._name=name
    def __str__(self):
        return "ID:"+str(self.id)+" Name:"+self._name
class NewUser(UserData):
    #def __init__(self,id,value):
    #    self.name=value
    #    self.id=id
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if(len(self._name)<3):
            return "ERROR"
        else:
            self._name=value
    def __call__(self):
        print(self._name+"'s id is "+str(self.id))

if __name__ == '__main__':
    user1=UserData(101,'Jack')
    user2=UserData(102,'Louplus')
    print(user1)
    print(user2)
    #user1 = NewUser(101, 'Jack')
    #user1.name='Lou'
    #user1.name='Jackie'
    #user1.set_name('Jackie')
    #user2 = NewUser(102, 'Louplus')
    #print(user1.name)
    #print(user2.name)
    user = NewUser(101, 'Jack')
    #user()
    
