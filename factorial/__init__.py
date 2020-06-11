import check50

@check50.check()
def exists():
    """factorial.py exists"""
    check50.exists("factorial.py")

@check50.check(exists)
def no_arguments():
    """no arguments"""
    check50.run("python factorial.py").stdout("Usage: python factorial.py <NUMBER>", regex=False).exit(1)

@check50.check(exists)
def non_integer_argument():
    """non-integer argument"""
    check50.run("python factorial.py foobar").stdout("You must provide an integer.", regex=False).exit(2)

@check50.check(exists)
def factorial_5():
    """factorial 5"""
    check50.run("python factorial.py 5").stdout("120", regex=False).exit(0)
