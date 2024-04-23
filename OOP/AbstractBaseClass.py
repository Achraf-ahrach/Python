# -------------------------------------------------------
# -- Object Oriented Programing => Abstract Base Class --
# -------------------------------------------------------

from abc import ABCMeta, abstractclassmethod

class Programming(metaclass=ABCMeta):

    @abstractclassmethod
    def has_oop(self):

        pass

    def has_name(self):
        pass

class Python(Programming):

    def has_oop(self):

        return "Yes"


class Pascal(Programming):

    def has_oop(self):

        return "No"

one = Python()

print(one.has_oop())