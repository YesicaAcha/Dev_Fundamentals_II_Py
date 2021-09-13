import abc


class Invoice(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_details(self):
        pass
