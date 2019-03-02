#!/usr/bin/env python3

class UserData:
    def __init__(self,id_one,name):
        self.id_one=id_one
        self.name=name
    def __repr__(self):
        return "ID:"+str(self.id_one)+" Name:"+self.name

class NewUser(UserData):
    group= 'shiyanlou-louplus'
    def get_name(self):
        return self.name
    def set_name(self,value):
        self.name=value
    @classmethod
    def get_group(cls):
        return cls.group
    @staticmethod
    def format_userdata(id_one,name):
        print(name+"'s id is "+str(id_one))

        
if __name__ == '__main__':
    #user1 = NewUser(101, 'Jack')
    #user1.set_name('Jackie')
    #user2 = NewUser(102, 'Louplus')
    #print(user1)
    #print(user2)
    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))
