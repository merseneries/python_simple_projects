import pytest
from email_slicer import check_valid_email


@pytest.mark.parametrize("input_email",
                         ["123@gmail.com", "ab@gmail.com", "ab@com", "ab@gmail.com", "@", "b@some.", "ukgmail.com"])
def test_invalid_input(input_email):
    assert check_valid_email(input_email) == False


@pytest.mark.parametrize("input_email",
                         ["bondps@bonansatours.com", "baliprestigeho@dps.centrin.net.id", "witamgr@dps.centrin.net.id",
                          "indahsuluh2002@yahoo.com.sg", "imz1991@yahoo.com"])
def test_valid_input(input_email):
    assert check_valid_email(input_email) == True
