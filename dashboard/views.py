from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dashboard/home.html')

def orderbook_bias(request):
    return render(request, 'dashboard/orderbook_bias.html')

def trader_bias(request):
    return render(request, 'dashboard/trader_bias.html')

def reddit_inst(request):
    return render(request, 'dashboard/reddit_posts.html')