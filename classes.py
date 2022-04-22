class Television:
    """
    A class representing details and actions of TV objects
    """

    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a TV object
        :param channel: which channel the tv object is on
        :param volume: how high/low the volume is for the tv object
        :param status: whether the tv object is on or off
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        """
        method to turn the tv object's status attribute on and off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def channel_up(self) -> None:
        """
        method to increase the channel attribute of the tv object
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        method to decrease the channel attribute of the tv object
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        method to increase the volume attribute of the tv object
        """
        if self.__status:
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        method to decrease the volume attribute of the tv object
        """
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        method to show all the attributes of a tv object in a formatted string
        :return: attributes of the tv object
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume} '
