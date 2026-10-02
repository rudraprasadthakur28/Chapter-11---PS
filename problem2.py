class Animals:
    pass

class Pets(Animals):
    pass


# class Dog(Pets):

#     @staticmethod
#     def bark():
#         print("Bow Bow!")


class Dog(Pets):

    def show(self):
        print("Bark")

dog = Dog()

dog.show()