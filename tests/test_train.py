import pytest

import utils


def test_load_data_should_raise_exception_when_data_not_found():
    with pytest.raises(FileNotFoundError):
        utils.load_data("dataset.csv")
