class Man:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name,'в возрасте',self.age)

    @staticmethod
    def compare_ages(man1,man2):
        if man1.age == man2.age:
            print("Ровестники")
        elif man1.age < man2.age:
            print(f"{man1.name} младше {man2.name}")
        else:
            print(f"{man2.name} младше {man1.name}")

man1 = Man('Вася',25)
man2 = Man('Петя',29)

Man.compare_ages(man1,man2)
print(111)
