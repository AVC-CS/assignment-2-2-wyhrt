import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = 'c\n23'
    sys.stdin = io.StringIO(datastr)

    celsius, fahrenheit = main.main() 
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # res = re.search(r'[\w,\W]*73\.40[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
    cs = celsius
    fs = fahrenheit
    assert cs == 23.0
    assert fs == 73.4


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = 'c\n35'
    sys.stdin = io.StringIO(datastr)

    celsius, fahrenheit = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    cs = celsius
    fs = fahrenheit
    assert cs == 35.0
    assert fs == 95.0
    # res = re.search(r'[\w,\W]*95[\w,\W]*', lines[0])
    # assert res != None
    # print(res.group())
