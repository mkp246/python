from  contextlib import closing
class RefrigeratorRaider:

    def open(self):
        print("opening....")

    def take(self, food):
        print("finding {} ...".format(food))
        if food == "A":
            raise RuntimeError("health waring!!")
        print("taking {} ..".format(food))

    def close(self):
        print("closing...")


def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        # r.close() auto call bu closing context

