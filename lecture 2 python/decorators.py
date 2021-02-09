def announce(f):
    def wrapper():
        print("Getting ready")
        f()
        print("Done")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()