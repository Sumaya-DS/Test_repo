from hello import more_hello, more_goodbye


def test_more_hello():
    assert "hi" == more_hello()


# make failer test


def test_more_goodbye():
    assert "bye" == more_goodbye()
