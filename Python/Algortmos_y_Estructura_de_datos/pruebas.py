class prueba():
    def __init__(self, valor) -> None:
        self._x = valor
    

    def getx(self):
        return self._x
    x = property(getx)


xd = prueba(5)
print(xd.getx())