
# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import Book


# 视图函数
def index(request):
  
    # render函数：载入模板，并返回context对象
    return render(request, 'iot/index.html')
    
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
    
    
 

 
    