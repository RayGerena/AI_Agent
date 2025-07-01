from functions.write_file import write_file

def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("RESULT FOR 'LOREM.TXT':")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print(result)
    print("")
    
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("RESULT FOR 'PKG/MORELOREM.TXT':")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print(result)
    print("")
    
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("RESULT FOR '/TMP/TEMP.TXT':")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print(result)
    print("")


if __name__ == "__main__":
    test()