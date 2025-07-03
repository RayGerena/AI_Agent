from functions.run_python_file import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print("RESULT FOR 'MAIN.PY':")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print(result)
    print("")
    
    result = run_python_file("calculator", "tests.py")
    print("RESULT FOR 'TESTS.PY':")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print(result)
    print("")
    
    result = run_python_file("calculator", "../main.py")
    print("RESULT FOR '../MAIN.PY':")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print(result)
    print("")
    
    result = run_python_file("calculator", "nonexistent.py")
    print("RESULT FOR 'NONEXISTENT.PY':")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print(result)
    print("")


if __name__ == "__main__":
    test()