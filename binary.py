


class Bin:
    def __init__(self, num):
        self.num = num

    def resto(self, numero, divisor):
        resto = int(numero % divisor)

        if resto != 0:
            #print(resto)
            return 1
        else:
            #print(resto)
            return 0


    def converter(self) -> list:
        result = []

        casa1 = self.num / 2
        resto = self.resto(self.num, 2)
        result.append(resto)

        casa2 = casa1 / 2
        resto = self.resto(casa1, 2)
        result.append(resto)

        casa3 = casa2 / 2
        resto = self.resto(casa2, 2)
        result.append(resto)

        casa4 = casa3 / 2
        resto = self.resto(casa3, 2)
        result.append(resto)


        return result[::-1]
    