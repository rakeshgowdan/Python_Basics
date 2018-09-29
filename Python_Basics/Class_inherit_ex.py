class Parent():
    def display(self):
        print("parent class")


class child(Parent):
    pass
    def display(self):
        print("child class")
p=Parent()
p.display()
c=child()
c.display()