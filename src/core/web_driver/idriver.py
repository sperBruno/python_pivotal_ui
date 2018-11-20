from abc import ABCMeta, abstractmethod


class IDriver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_driver(self):
        pass