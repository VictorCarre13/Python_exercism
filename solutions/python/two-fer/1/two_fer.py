def two_fer(name=None):
    try:
        if name is None:
            name="you"
        return f"One for {name}, one for me."
    except TypeError:
        return f"One for you, one for me."