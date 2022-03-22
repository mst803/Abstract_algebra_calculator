from math import gcd, modf
from django.http import HttpResponse
from django.shortcuts import render


# mult inverse
def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return 'no inverse'

# add inverese
def mod(a, b):
    if b>a:
        d  = b - a
        return d
    elif b==a:
        return 0
    else:
        return mod(a%b,b)




def mult_inverse(request):
    if request.method == 'POST':
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        inverse = modInverse(a, b)
        g = gcd(a, b)

        return render(request, 'display_mul.html', {
            'a': a,
            'b': b,
            'g': g,
            'i': inverse
        })
    return render(request, 'form_mul.html')



def add_inverse(request):
    if request.method == 'POST':
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        inverse = mod(a, b)

        return render(request, 'display_add.html', {
            'a': a,
            'b': b,
            'i': inverse
        })
    return render(request, 'form_add.html')

def home(request):
    return render(request, 'home.html')