import pytest
from television import *

class TestTelevision:

    def test_init(self):
        tv = Television()
        state = str(tv)
        assert "Power = False" in state
        assert "Channel = 0" in state
        assert "Volume = 0" in state

    def test_power(self):
        tv = Television()
        state = str(tv)
        assert "Power = False" in state
        # test Power on
        tv.power()
        state = str(tv)
        assert "Power = True" in state
        # test power off
        tv.power()
        state = str(tv)
        assert "Power = False" in state


    def test_mute(self):
        tv = Television()
        state_first = str(tv)
        tv.mute() # calling mute == false
        state_sec = str(tv) #
        # Test mute function when the tv is powered off by comparing the state using the mute function 
        assert state_sec == state_first

        # Powering on TV
        tv.power()
        state_sec = str(tv)

        # Check if tv is powered on
        assert "Power = True" in state_sec

        # Check if Mute is set to false
        assert tv._Television__muted is False

        tv.mute() # called the mute function

        assert tv._Television__muted is True # checks if mute is set to True

        tv.mute() # call function again

        assert tv._Television__muted is False # checks if mute is set to false


    def test_channel_up(self):
        pass
    def test_channel_down(self):
        pass
    def test_volume_up(self):
        pass
    def test_volume_down(self):
        pass


if __name__ == '__main__':
    pytest.main()