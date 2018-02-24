from django.shortcuts import render
from app01.models import Zhilian
from django.core.paginator import Paginator
# Create your views here.

def index(request,pIndex=1):
    #执行数据查询,并防止到模板
    list = Zhilian.objects.all()
    #判断并封装搜索条件
    where = [] #定义一个用于维持搜索条件的变量
    if request.GET.get('pname','') != '':
        print(request.GET.get('pname'))
        list = list.filter(pname__contains=request.GET.get('pname'))
        where.append('pname='+request.GET.get('pname'))
    #传入数据和页大小来创建分页对象
    p = Paginator(list,100)
    #判断页号没有值时初始化为1
    if pIndex == '':
        pIndex = 1
    pIndex = int(pIndex)#类型转换
    list2 = p.page(pIndex)#获取当前页数
    plist = p.page_range #获取页码信息
    if len(plist) >= 10:
        plist = plist[:10]
    #封装分页信息
    context = {'zhilianlist' : list2,'plist' : plist,'pIndex' : pIndex,'where':where}
    return render(request, 'index.html', context)