from datetime import datetime


class  SMS_store():

    def __init__(self):

        self.store = []

    def __str__(self):
        return("{0}".format(self))

    def  add_new_arrival(self,number,time, text):
        self.store.append(("Read : False","From : " + number,"Received : "+ time,"Msg: "+text))


    def message_count(self):
        return(len(self.store))

    
    def get_unread_messages(self):
        result = []
        for i,m in enumerate(self.store):
            if m[0] == "Read : False":
                result.append(m)
        return(result)

    def get_message(self, i):
        
        if i < len(self.store):
            msg = self.store[i]
            msg = ("Read: True",) + msg[1:] # Tuples are immutable so msg[i][0] = " Read : True" is not valid
            self.store[i] = (msg)
            return (self.store[i][1:])
        else:
            return None

    def delete(self,i):
        del self.store[i]
    
    def clear(self):

        self.store = []


my_inbox = SMS_store()

my_inbox.add_new_arrival("925002859","18","Hello")
my_inbox.add_new_arrival("925002859","18:30","Are you okay ?")
my_inbox.add_new_arrival("925002859","19:00","Your tests are lame ...")


print(my_inbox.get_unread_messages())

print("\n")

print(my_inbox.get_message(2))

print("\n")

print(my_inbox.get_unread_messages())

my_inbox.delete(1)

print("\n")

print(my_inbox.get_unread_messages())


