import pytest
from television import *

class Test_Television:

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
        state = str(tv)
        assert "Mute = False" in state

    def test_volume(self):
        pass



