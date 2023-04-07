from abc import ABC,abstractmethod

class Work(ABC):
    @abstractmethod
    def get_info_work(self):
        pass

class Employee(ABC):
    @abstractmethod
    def get_info(self):
        pass

class SeniorDeveloper(Employee,Work):
    def get_info_work(self):
        print("Информация о должностной инструкции ведущего программиста")

    def get_info(self):
        print("Информация общая о ведущем программисте")

class JuniorDeveloper(Employee):

  def get_info(self):
        print("Информация общая о стажоре")

JuniorDeveloper().get_info()