from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homePageView(request):
    return HttpResponse("Hello, World!")

new_str = "There are 223 apples 1234567890 for 4151242352 d 8945134894"
new_str = new_str.replace(" ", "")
char = "abcdefghijklmnopqrstuvwxyz"

for i in char:
    new_str = new_str.replace(i, "," + i + ",").replace(",,", ",")
new_str = new_str.split(",")

number = []
for i in range(0, len(new_str)):
    if len(new_str[i]) == 10:
        if new_str[i].isdigit():
            number.append(new_str[i])


def writetofile(request):
    testfile = open('./media/data.txt', 'w')
    testfile.writelines('\n'.join(number))
    testfile.close
    return HttpResponse()


def readfile(request):
    f = open('./media/data.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)
    return HttpResponse(f'<p>{contents}</p>')
