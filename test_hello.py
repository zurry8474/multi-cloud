from hello import speak


def test_speak():
    assert "Bob" in speak("Bob")
    