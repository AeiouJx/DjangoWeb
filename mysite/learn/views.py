# -*- coding: utf-8 -*-
# learn/views.py

from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.http import FileResponse
from django.http import StreamingHttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
import os
from django.conf import settings 

from .models import Information

from datetime import datetime

# 主页
def index(request):
    context = { 
       
    }
    # render函数：载入模板，并返回context对象
    return render(request, 'learn/home.html', context)

# 网站信息
def info(request):
    info_list = Information.objects.all()
    context = {
        'info_list': info_list,
    }
    return render(request, 'learn/info.html', context)

# 留言功能
@login_required(login_url='/userprofile/login/')
def msgproc(request):
    datalist=[]
    if(request.method=="POST"):
        userA=request.POST.get("userA",None)
        userB=request.POST.get("userB",None)
        msg=request.POST.get("msg",None)
        time=datetime.now()
        with open('msgdata.txt','a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB,userA,msg,time.strftime("%Y-%m-%d %H:%M:%S")))

    if(request.method=="GET"):
        userC=request.GET.get("userC",None)
        if(userC!=None):
            with open('msgdata.txt','r') as f:
                cnt=0
                for line in f:
                    linedata=line.split('--')
                    if(linedata[0]==userC):
                        d={"userA":linedata[1],"msg":linedata[2],"time":linedata[3]}
                        datalist.append(d)
                    if(cnt>=10):
                        break
    # render函数第三个参数是字典类型，表明向html页面中特                    
    return render(request,"learn/MsgSingleWeb.html",{"data":datalist})  
    

# 文件下载
def downloadfile(request,path):
    # file_name = request.GET["file"]
    
    file_path = os.path.join(settings.BASE_DIR,path)    # 下载文件的绝对路径
    print(file_path)
    
    if not os.path.isfile(file_path):  # 判断下载文件是否存在
        return HttpResponse("Sorry but Not Found the File") # 不存在
    
    def file_iterator(file_path, chunk_size=512):
        """
        文件生成器,防止文件过大，导致内存溢出
        :param file_path: 文件绝对路径
        :param chunk_size: 块大小
        :return: 生成器
        """
        with open(file_path, mode='rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    try:
        response = StreamingHttpResponse(file_iterator(file_path))
        # response = HttpResponse(open(file_path, 'rb'))
        # response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name)
    except:
        return HttpResponse("Sorry but Not Found the File")
    
    return response
    
    
    
    
    
    
    
    