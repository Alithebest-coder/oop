class parrot:
    species="BIRD"
    def __init__(self,name,age):
        self.a=name
        self.g=age
obj=parrot("bob",1)
obj2=parrot("bob jr",0)
print (obj.species,obj.a,obj.g)
print (obj2.species,obj2.a,obj2.g)