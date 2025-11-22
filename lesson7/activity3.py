class bird:
    type="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
sparrow=bird("sparrow",10)
crow=bird("crow",15)
print("sparrow is a: ",sparrow.type)
print("crow is a: ",crow.type)
print("name: ",sparrow.name,"age: ",sparrow.age)
print("name: ",crow.name,"age: ",crow.age)
