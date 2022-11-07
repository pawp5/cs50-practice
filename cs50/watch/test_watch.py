from watch import parse

def test_www():
    assert parse('<iframe src="https://www.youtube.com/embed/3KZYmACVmYQ"></iframe>') == "https://youtu.be/3KZYmACVmYQ"

def test_http():
    assert parse('<iframe src="http://youtube.com/embed/3KZYmACVmYQ"></iframe>') == "https://youtu.be/3KZYmACVmYQ"

def test_https():
    assert parse('<iframe src="https://youtube.com/embed/3KZYmACVmYQ"></iframe>') == "https://youtu.be/3KZYmACVmYQ"

def test_invalid():
    assert parse('<iframe src="https://www.instagram.com/__pawps/"></iframe>') == None