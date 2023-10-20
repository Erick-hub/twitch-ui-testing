import pytest


@pytest.mark.usefixtures("get_driver", "get_game_name")
class BaseTest():
    pass
