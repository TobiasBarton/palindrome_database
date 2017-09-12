from datetime import datetime
import uuid


class Palindrome:
    """
    Class for controling the formating for storing palindrome strings and other 
    useful properties.
    :param: palindrome_str - palindrome string
    """
    __palindrome_str = None
    __time_added = None
    __id = None

    def __init__(self, palindrome_str):
        self.__id = uuid.uuid4()
        self.palindrome_str = palindrome_str
        self.time_added = datetime.now()

    # Properties

    @property
    def id(self):
        return self.__id

    @property
    def time_added(self):
        return self.__time_added

    @time_added.setter
    def time_added(self, value):
        self.__time_added = value

    @property
    def palindrome_str(self):
        return self.__palindrome_str

    @palindrome_str.setter
    def palindrome_str(self, value):
        self.__palindrome_str = value

    # Methods

    def serialize(self):
        return {
            "palindrome_str": self.palindrome_str,
            "id": self.id,
            "time_added": self.time_added

        }
