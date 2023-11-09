class TEAMA:
    member = 0 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        TEAMA.member +=1
    def get_yob(self):
        return 2023 - self.age