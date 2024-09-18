class person:
     def __init__(self,age,gender):
        self.gender = gender
        self.age= age


     def myintro(self):
      print("Hello my gender is" ,self.gender)
      print("Hello my age is",self.age)
harry= person("mail",36)
sarrah=person("femail",34)
harry.myintro()
sarrah.myintro()
