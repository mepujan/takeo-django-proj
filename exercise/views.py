from django.http import HttpResponse
from datetime import datetime
from random import choice

# Create your views here.

def format_date_time(response):
    today_date_time = datetime.now()
    print(today_date_time)
    formatted_date_time = today_date_time.strftime("%a,%d %b, %Y %I:%M:%S %p")
    return HttpResponse(formatted_date_time)


def acccess_quote(response):
    quotes = [
        "The purpose of our lives is to be happy. - Dalai Lama" ,
        "Get busy living or get busy dying. — Stephen King",
        "You only live once, but if you do it right, once is enough. — Mae West"
    ]
    choosen_quote = choice(quotes)
    return HttpResponse(choosen_quote)