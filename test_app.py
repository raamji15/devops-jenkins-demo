from app import greet


def test_greet():
    assert greet("Jenkins") == "Hello, Jenkins! DevOps pipeline is working."
