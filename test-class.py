class thisClass():
    def __init__(self, numberz):
        self.number = numberz

    def greet(self):
        print(f"Hello {self.number}")

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = MyClass('5')
print(p.name)
p.greet()

q = thisClass(3)
print(q.number)
q.greet()