class CurrentBoxNotifier:

    def __init__(self):
        self.current_box_observers = []

    def add_box_observer(self, observer):
        self.current_box_observers.append(observer)

    def remove_box_observer(self, observer):
        self.current_box_observers.remove(observer)

    def call_box_observers(self,current_box):
        for o in self.current_box_observers:
            o.update(current_box)
