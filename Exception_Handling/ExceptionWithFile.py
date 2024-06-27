
try:
    f = open("dummyfile")
    try:
        f.write("Hey Aditya This Side")
    except:
        print("There is some issue while writing the text in the file.")
    finally:
        f.close()
except:
    print("No such file exist.")
