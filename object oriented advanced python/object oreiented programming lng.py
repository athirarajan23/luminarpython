# class: design pattern
# object:real world entity
# references: name that refers a memory location of a object

#
# class name must start with a capital letter.
# self is an instance keyword

class Person:
    def walk(self):
        print("he is walking")
    def jump(self):
        print("he is jumping")
obj=Person()    #any number of object can be created using diff references here obj is h=the reference.
obj.walk()
obj.jump()
obj2=Person()
obj2.walk()
obj2.jump()
