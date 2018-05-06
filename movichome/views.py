from django.shortcuts import render,HttpResponse
from .scrap import mainDbpScrape, mainMcpScrape
from django.http import HttpResponse
from .models import PageScrape

def index(request):
    # return HttpResponse('Hello world')
    return render(request, 'home.html')
    
def result(request):
    PageScrape.objects.all().delete()
    userinput = request.POST.get('userkeyword', None)
    userkeywords = userinput

    #website satu
    dpbresult = mainDbpScrape.dbp()
    dpbresult.scrapeItem(userkeywords)

    #website dua
    mcpresult = mainMcpScrape.mcp()
    mcpresult.scrapeItem(userkeywords)

    item = PageScrape.objects.all()
    return render(request, 'search.html', {'desc': item})
