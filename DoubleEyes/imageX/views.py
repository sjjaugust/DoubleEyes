from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .utils.rectify import rectify # 矫正函数
from .utils.fourStickman import four_stickman   # 立体匹配函数
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
        image1 = request.FILES.get('image1')
        pic_0_name, pic_1_name = 'pic_0.png', 'pic_1.png'
        pic_0_path = os.path.join(settings.IMG_URL, pic_0_name)
        pic_1_path = os.path.join(settings.IMG_URL, pic_1_name)
        output_0 = open(pic_0_path, 'wb')
        output_1 = open(pic_1_path, 'wb')
        for chunk in image0.chunks():  # 分块写入文件
            output_0.write(chunk)
        for chunk in image1.chunks():  # 分块写入文件
            output_1.write(chunk)
        # 关闭文件流
        output_0.close()
        output_1.close()

        # 矫正图片
        rec_0_name, rec_1_name = 'rectify_0.png', 'rectify_1.png'
        rec_0_path = os.path.join(settings.IMG_URL, rec_0_name)
        rec_1_path = os.path.join(settings.IMG_URL, rec_1_name)
        rectify(pic_0_path, pic_1_path, rec_0_path, rec_1_path)

        four_stickman()
        context = {'success': 1}
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        return HttpResponse('500 no')



