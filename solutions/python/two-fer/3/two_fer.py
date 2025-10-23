"""Module implementing the 'two_fer' function."""

def two_fer(name=None):
    if name is None:
        name="you"
    return f"One for {name}, one for me."
