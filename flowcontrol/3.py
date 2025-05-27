def bar_code_scanner(serial):
    match serial:
        case "123":
            print("Product1")
        case "113":
            print("Product2")
        case "142":
            print("Product3")
        case _:
            print("Product not found!")


bar_code_scanner("113")
bar_code_scanner(142)
# It will print Product2 and Product not found!. Since argument for second call is integer instead of string it will be not considered same as "142".
