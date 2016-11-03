def correct(x):
    y = x.split()
    y = list(y)
    for i in y:
        if i == " ":
            for o in y:
                if o == " ":
                    y.remove(o)
        y.insert(y.index(i)," ")
        if i == ".":
            y.insert(y.index(i)+1," ")
    y = " ".join(y)
    return y

print(correct("This   is  very funny  and    cool.Indeed!"))

