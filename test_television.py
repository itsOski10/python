import pytest
from television import *

class TestTelevision:

    def test_init(self):
        tv = Television()
        state = str(tv)
        assert  state == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        tv = Television()
        state = str(tv)
        assert state == "Power = False, Channel = 0, Volume = 0"

        # test Power on
        tv.power()
        state = str(tv)
        assert state == "Power = True, Channel = 0, Volume = 0"

        # test power off
        tv.power()
        state = str(tv)
        assert state == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        tv = Television()

        # Mute when TV is OFF → no change
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"
        tv.mute()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

        # Turn TV ON
        tv.power()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

        # First mute → muted ON (volume should display as MIN_VOLUME = 0)
        tv.mute()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

        # Second mute → muted OFF (volume should return to real volume = 0)
        tv.mute()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"


    def test_channel_up(self):
        tv = Television()
        tv.power()  # turn on

        tv.channel_up()  # 0 -> 1
        assert str(tv) == "Power = True, Channel = 1, Volume = 0"

        tv.channel_up()  # 1 -> 2
        assert str(tv) == "Power = True, Channel = 2, Volume = 0"

        tv.channel_up()  # 2 -> 3
        assert str(tv) == "Power = True, Channel = 3, Volume = 0"

        tv.channel_up()  # 3 -> 0 wrap
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

        tv.channel_up()  # 0 -> 1 again
        assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    def test_channel_down(self):
        tv = Television()
        tv.power()  # turn on

        tv.channel_down()  # 0 -> 3 wrap
        assert str(tv) == "Power = True, Channel = 3, Volume = 0"

        tv.channel_down()  # 3 -> 2
        assert str(tv) == "Power = True, Channel = 2, Volume = 0"

        tv.channel_down()  # 2 -> 1
        assert str(tv) == "Power = True, Channel = 1, Volume = 0"

        tv.channel_down()  # 1 -> 0
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

        tv.channel_down()  # 0 -> 3 again
        assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        tv = Television()

        # Off: no change
        tv.volume_up()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

        # On: increase
        tv.power()
        tv.volume_up()  # 0 -> 1
        assert str(tv) == "Power = True, Channel = 0, Volume = 1"

        # Muted: unmute + increase
        tv.mute()
        tv.volume_up()  # should unmute + go to 2
        assert str(tv) == "Power = True, Channel = 0, Volume = 2"

        # Try to exceed max volume
        tv.volume_up()  # stays at 2
        assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        tv = Television()

        # Off: no change
        tv.volume_down()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

        # On and increase volume first
        tv.power()
        tv.volume_up()  # 0 -> 1
        tv.volume_up()  # 1 -> 2
        assert str(tv) == "Power = True, Channel = 0, Volume = 2"

        # Volume down (2 -> 1)
        tv.volume_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 1"

        # Muted: unmute + decrease
        tv.mute()
        tv.volume_down()  # unmute + 1 -> 0
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

        # Stays at min (0 -> 0)
        tv.volume_down()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"


if __name__ == '__main__':
    pytest.main()