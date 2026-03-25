def func(a: str, b: str):
    # Local Variables
    a = "100"
    b = "200"
    print(f"Id of a ={id(a)}. Id of b = {id(b)}")


# Int,str
a = "Anirudh"
b = "Khurana"
print(f"Id of a ={id(a)}. Id of b = {id(b)}")
func(a, b)
print(a)
print(b)
