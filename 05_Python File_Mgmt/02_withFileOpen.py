def Main():
    wordlist = ["cat", "has", "a", "rat"]
    with open("new_demo.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")
        f.close()



if __name__ == "__main__":
    Main()