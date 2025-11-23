class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL:int = 0
    MAX_CHANNEL:int = 3

    def __init__(self) -> None:
        """Initialize the Television with default power, volume, and channel settings."""
        self.__status:bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel:int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the TV’s power state between on and off"""

        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """Toggle the mute state, but only when the TV is powered on."""
        if not self.__status:
            return
        else:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """Increase channel,wrap around MIN_CHANNEL if MAX_CHANNEL is reached"""
        if not self.__status:
            return
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1

    def channel_down(self) -> None:
        """Decrease channel, wrap around if MAX_CHANNEL if MIN_CHANNEL is reached """
        if not self.__status:
            return
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1

    def volume_up(self) -> None:
        """changes the volume status of the television by one up"""
        if not self.__status:
            return
        if self.__status == True and self.__muted == True:
            self.__muted = False
        if self.__volume < Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """changes the volume status of the television by one down"""
        if not self.__status:
            return
        if self.__status == True and self.__muted == True:
            self.__muted = False
        if self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        """Return a string representation of the television"""
        if self.__muted:
            displayed_volume:int = Television.MIN_VOLUME
        else:
            displayed_volume:int = self.__volume

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {displayed_volume}"