from django.shortcuts import render, HttpResponse

# Create your views here.
def soma(requests, num1, num2):
     resultado = (int(num1) + int(num2))
     return HttpResponse('<h1>Soma de {} e {} é igual à {} </h1>'.format(num1, num2, resultado))

def subtracao(requests, num1, num2):
    resultado = (int(num1) - int(num2))
    return HttpResponse('<h1>Subtração de {} com {} é igual à {} </h1>'.format(num1, num2, resultado))

def multiplicacao(requests, num1, num2):
    resultado = (int(num1) * int(num2))
    return HttpResponse('<h1>Multiplicação de {} e {} é igual à {} </h1>'.format(num1, num2, resultado))