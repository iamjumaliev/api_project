from django.shortcuts import render
import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def json_add_view(request, *args, **kwargs):
    data = None
    print(request.body)
    if request.body:
        data = json.loads(request.body)
        a = data['A']
        b = data['B']
        if type(a) == int and type(b) == int:
            sum = a + b
            answer = {
            "answer": sum
            }
            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
            response['Content-Type'] = 'application/json'
            return response
        else:
            response = JsonResponse({'error': 'Wrong data!'})
            response.status_code = 400
            return response
    else:
        response = JsonResponse({'error': 'Wrong data!'})
        response.status_code = 400
        return response


@csrf_exempt
def json_substract_view(request, *args, **kwargs):
    data = None
    print(request.body)
    if request.body:
        data = json.loads(request.body)
        a = data['A']
        b = data['B']
        if type(a) == int and type(b) == int:
            subs = a - b


            answer = {
            "answer": subs
            }

            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
            response['Content-Type'] = 'application/json'
            return response
        else:
            response = JsonResponse({'error': 'Wrong data!'})
            response.status_code = 400
            return response
    else:
        response = JsonResponse({'error': 'Wrong data!'})
        response.status_code = 400
        return response


@csrf_exempt
def json_multiply_view(request, *args, **kwargs):
    data = None
    print(request.body)
    if request.body:
        data = json.loads(request.body)
        a = data['A']
        b = data['B']
        if type(a) == int and type(b) == int:
            multi = a*b


            answer = {
            "answer": multi
            }

            answer_as_json = json.dumps(answer)
            response = HttpResponse(answer_as_json)
            response['Content-Type'] = 'application/json'
            return response
        else:
            response = JsonResponse({'error': 'Wrong data!'})
            response.status_code = 400
            return response
    else:
        response = JsonResponse({'error': 'Wrong data!'})
        response.status_code = 400
        return response


@csrf_exempt
def json_divide_view(request, *args, **kwargs):
    data = None
    print(request.body)
    if request.body:
        data = json.loads(request.body)
        a = data['A']
        b = data['B']
        if type(a) == int and type(b) == int:
            if b == 0:
                response = JsonResponse({'error': 'Division by zero!'})
                response.status_code = 400
                return response
            else:
                div = a // b
                answer = {
                "answer": div
                }
                answer_as_json = json.dumps(answer)
                response = HttpResponse(answer_as_json)
                response['Content-Type'] = 'application/json'
                return response
        else:
            response = JsonResponse({'error': 'Wrong data!'})
            response.status_code = 400
            return response
    else:
        response = JsonResponse({'error': 'Wrong data!'})
        response.status_code = 400
        return response

# Create your views here.
