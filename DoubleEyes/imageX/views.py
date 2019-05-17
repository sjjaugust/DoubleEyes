from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from base64 import b64decode
import json
import re
import os
def index(request):
    """
    主页面显示
    :param request:
    :return:
    """
    data = {
        "status": "success!",
    }
    return render(request, 'imageX/index.html', locals())


@csrf_exempt
def uploadimg(request):
    if request.method == 'POST':
        # 以POST方式得到base64 图片编码

        image0 = request.FILES.get('image0')
        # print(image0)
        image1 = request.FILES.get('image1')
        # print(image1)

        # # 这里是对base64编码的格式化
        # imgstr0 = re.search(r'base64,(.*)', imgdata['pic_0']).group(1)
        # imgstr1 = re.search(r'base64,(.*)', imgdata['pic_1']).group(1)
        #
        # # 文件保存到本地
        output_0 = open(os.path.join(settings.IMG_URL, 'pic_0.png'), 'wb')
        output_1 = open(os.path.join(settings.IMG_URL, 'pic_1.png'), 'wb')
        for chunk in image0.chunks():  # 分块写入文件
            output_0.write(chunk)
        for chunk in image1.chunks():  # 分块写入文件
            output_1.write(chunk)
        # 关闭文件流
        output_0.close()
        output_1.close()
        context = {'success': 1}
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponse('500 no')