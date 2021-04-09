var1 = 0
var2 = 99


def my_var_changer():
    global var2
    var1 = 37
    var2 = 13
    global var3
    var3 = 8547465


print("var1 before", var1)
print("var2 before", var2)


my_var_changer()

print("var1 after", var1)
print("var2 after", var2)
print(var3)