def readFile():
    try:
        f = open("brrrr.txt", "r")
        for line in f:
            print(line.strip("\n""\r"))
        f.close()
    except:
        print("Some error: either with the file or with the permission")
    finally:
        print("Exiting the loop!")


def Main():
    readFile()

if __name__ == "__main__":
    Main()