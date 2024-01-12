from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound, HttpResponseServerError, \
    HttpResponseBadRequest, HttpResponseForbidden
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.urls import reverse
import cgi

from metroApp.models import Metro, Drivers

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Инфо', 'url_name': 'reg'},
        {'title': 'Справка по трамваям', 'url_name': 'courses'},
        {'title': 'Схема метро', 'url_name': 'help'},
        {'title': 'Контакты', 'url_name': 'about'}
        ]


def home(request):

    data = {'menu': menu,}
    return render(request, 'home/home.html', context=data)
def drivers(request):
    d = Drivers.objects.all()
    data = {
        'd': d,

    }

    return render(request, 'drivers/drivers.html', context=data)


def info(request):
    return render(request, 'info/info.html')


def contacts(request):
    return render(request, 'contacts/contacts.html')


# def spravka(request):
# return render(request, 'spravka/spravka.html')


def schema(request):
    return render(request, 'schema/schema.html')


# Create your views here.
def spravkaM(request, slug):
    m = Metro.objects.all()
    slug = get_object_or_404(Metro, slug=slug)
    data = {
        'm': m,
        'slug': slug,
    }
    return render(request, 'spravka/spravka.html', context=data)



def create(request):
    if request.method == "POST":
        m = Metro()
        m.route = request.POST.get("route")
        m.depo = request.POST.get("depo")
        m.depo = request.POST.get("depo")
        m.exit1 = request.POST.get("exit1")
        m.exit2 = request.POST.get("exit2")
        m.plan1 = request.POST.get("plan1")
        m.plan2 = request.POST.get("plan2")
        m.brak = request.POST.get("brak")
        m.zader = request.POST.get("zader")
        m.snizh_dkr_kr = request.POST.get("snizh_dkr_kr")
        m.snizhskor = request.POST.get("snizhskor")
        m.pereklpotu = request.POST.get("pereklpotu")
        m.itogo = request.POST.get("itogo")
        m.itogoproc = request.POST.get("itogoproc")
        m.flightwithoutplan = request.POST.get("flightwithoutplan")
        m.srskor = request.POST.get(" srskor")
        m.srskorplan = request.POST.get("srskorplan")
        m.save()
    return HttpResponseRedirect("/")


def add(request):
    if request.method == "POST":
        d = Drivers()
        id_driver = request.POST.get("id_driver","")
        name = request.POST.get("name","")
        tram_number = request.POST.get("tram_number","")
        d.id_driver = id_driver
        d.name = name
        d.tram_number = tram_number
        d.save()
    return render(request, "add/add.html")


def delete_object_function(request):
    # OrderSparePart is the Model of which the object is present

    ob = Drivers.objects.all()
    ob.delete()
   # a = cgi.FieldStorage()
    #searchterm = a.getvalue('delete')

    return render(request,"drivers/drivers.html")
def pageNotFound(request, exception):
    data = {'error': 'Ошибка 404: такой страницы нет :('}
    return render(request, 'error.html', context=data)


def serverError(request):
    data = {'home': home,
            'error': 'Ошибка 500: сервер сломался, скоро починю :('}
    return render(request, 'error.html', context=data)


def badRequest(request, exception):
    data = {'header': home,
            'error': 'Ошибка 400: Сайт не может прожевать ваш запрос :('}
    return render(request, 'error.html', context=data)


def forbidden(request, exception):
    data = {'header': home,
            'error': 'Ошибка 403: Страница заброшена или перемещена по другому адресу :('}
    return render(request, 'error.html', context=data)
