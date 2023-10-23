from string import ascii_letters


def test_method_1 ():
    assert clear_text("text test") == "text test"
        
def test_method_2 ():
    assert clear_text ("TEXT TEST"), "text test"
    
def test_method_3 ():
    assert clear_text ("text-test"), "texttest"

def test_method_4 ():
    assert clear_text ("text РУССКИЙ test") == "text  test"

def test_method_5 ():
    assert clear_text ("TEXT РУССКИЙ-123-test") == "text test"

def test_method_6 ():
    assert clear_text () == "text test"


def clear_text (text: str):

    result = ""
    for i in text:
        if i in ascii_letters + " ":
            result += i
    return result.lower()