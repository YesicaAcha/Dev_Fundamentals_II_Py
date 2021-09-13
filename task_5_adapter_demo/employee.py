import abc


class Employee(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_id(self):
        pass

    @abc.abstractmethod
    def get_firstname(self):
        pass

    @abc.abstractmethod
    def get_lastname(self):
        pass

    @abc.abstractmethod
    def get_email(self):
        pass
