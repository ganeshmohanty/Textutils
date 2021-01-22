from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #return HttpResponse("hello ganesh")
    return render(request,'index.html')


def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')

    #check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlinerm=request.POST.get('newlinerm','off')
    extraspacerm=request.POST.get('extraspacerm','off')
    charatctercount=request.POST.get('charactercount','off')
    #print(removepunc)

    #check which checkbox value is on and anlyze according to that
    if removepunc=="on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punc:
                analyzed=analyzed + char
        parameters={'purpose':'Remove Punctuations','textt': analyzed}
        djtext=analyzed
        #return HttpResponse("remove punctuation")
        #return render(request,'analyze.html',parameters)

    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        parameters={'purpose':['purpose','Changed to UPPER Case'],'textt':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',parameters)
        
    if(newlinerm=='on'):
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed=analyzed+char
        parameters={'purpose':['purpose','New lines Removed'],'textt':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',parameters)

    if (extraspacerm=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        parameters={'purpose':['purpose','Extra Space Removed'],'textt':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',parameters)

    if (charatctercount=='on'):
        counter=0
        for i in djtext:
            counter=counter+1
        analyzed=f"The Number Of Character in Your String is {counter}"
        parameters={'purpose':'Character Counter','textt':analyzed}
        #djtext=analyzed
        #return render(request,'analyze.html',parameters)


    #else:
        #return HttpResponse("Error")
    if (charatctercount !='on' and extraspacerm !='on' and newlinerm !='on' and fullcaps !='on' and removepunc !='on' and charatctercount !='on' and extraspacerm !='on'):
        return HttpResponse("Error! Atleast Select One Option")
    return render(request,'analyze.html',parameters)

def about(request):
    #return HttpResponse("this web app is created by ganesh ")
    return render(request,'about.html')

    

"""def removespace(request):
    return HttpResponse("remove Space ")

def newline(request):
    return HttpResponse("newline")

def charcount(request):
    return HttpResponse("count the characters")
    

def capfirst(request):
    return HttpResponse("capitilize first")
    
"""