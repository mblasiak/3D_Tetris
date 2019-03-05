class Score:
    def __init__(self):
        self.score = 0
        self.observers=[]

    def inc(self):
        self.score += 1
        self.call_observer()

    def reset(self):
        self.score = 0
        self.call_observer()

    def add_observer(self,observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        self.observers.remove(observer)

    def call_observer(self):
        for o in self.observers:
            o.update(self.score)
