from django.shortcuts import render

# Create your views here.
def landingpage(request):
    context = {

    }
    return render(request, 'landingpage.html', context)