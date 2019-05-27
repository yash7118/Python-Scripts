def Main():

    list = ["cat","with","a","hat","sat","on","my","sofa"]

    f = open("demo.txt", "w")
    for _ in list:
        f.write(_ + "\n")
    f.close()

if __name__ ==  "__main__":
    Main()