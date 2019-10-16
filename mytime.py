class MyTime:


    def __init__(self, hrs= 0, mins = 0, secs = 0):

        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    
    def __str__(self):
        return("{0}:{1}:{2}".format(self.hours,self.minutes, self.seconds))


    def increment(self,seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60 
            self.hours += 1 



    def to_seconds(self):
        return self.hours * 3600 + self. minutes * 60 + self.seconds

time = MyTime(10,21,34)

print(time)


# Pure function - Add time
# 

def add_time(t1,t2):
    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds 
    sum_t = MyTime(h,m,s)
    return sum_t


current_time = MyTime(9,14,30)
bread_time = MyTime(3, 35, 0)
done_time = add_time(current_time, bread_time)
print(done_time)


def increment(t, secs):
    t.seconds += secs

    while t.seconds >= 60:
        t.seconds -= 60
        t.minutes +=1

    while t.minutes >= 60:
        t.minutes -= 60
        t.hours += 1 




print(bread_time)

increment(bread_time,200)

print(bread_time)

bread_time.increment(200)

print(bread_time)


class MyTime2:

    def __init__(self,hrs = 0, mins = 0, secs = 0):

        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60 




def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)