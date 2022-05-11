from django.shortcuts import render
def index(request):
    return render(request,'about.html')
def counter(request):
    t=request.POST['text']
    n=int(t)
    sum=0
    while n>0:
        d=n%10
        sum=sum+d
        n=n//10
    return render(request, 'counter.html', {'sod': sum})


    #text = request.POST['text']
    #amount_of_words = len(text.split())


# Create your views here.
