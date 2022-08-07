from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests

# Create your views here.

def index(request):
    """
    Index page
    """
    return render(request, 'main/index.html')

def checkout(request):

    if request.method == "GET":
        return render(request, "main/checkout.html")

    if request.method == "POST":
        context = { "amount": 1000.00, "order_id": "HHBNHHJH7HVHJB", "return_url": "https://enairagwtest.pythonanywhere.com/return" }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token fecc39ea8c9f69a2d9d9405514b9964edaaf48b3"
        }
        res = requests.post("https://enairagw.pythonanywhere.com/api/payment/intent", headers=headers, json=context )
        if res.status_code == 201:
            response = res.json()
            print(response)
            return HttpResponseRedirect(response["redirect_url"])
        else:
            val = res.status_code
            return HttpResponse(f"Unable to process payment at the moment {val}")

def return_view(request):
    return render(request, "main/success.html")


