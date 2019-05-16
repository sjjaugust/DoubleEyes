from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from django.shortcuts import get_object_or_404


def index(request):
    """
    资产总表视图
    :param request:
    :return:
    """
    data = {
        "status": "success!",
    }
    return render(request, 'imageX/index.html', locals())