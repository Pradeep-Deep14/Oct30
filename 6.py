def foo(x,y=[]):
    y.append(x)
    return y

print(foo(2))
print(foo(3))


#[2]
#[2,3]