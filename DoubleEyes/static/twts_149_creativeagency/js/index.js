var imgFile = []; //文件流
var imgSrc = []; //图片路径
var imgName = []; //图片名字
$(function(){
	// 鼠标经过显示删除按钮
	$('.content-img-list').on('mouseover','.content-img-list-item',function(){
		$(this).children('a').removeClass('hide');
	});
	// 鼠标离开隐藏删除按钮
	$('.content-img-list').on('mouseleave','.content-img-list-item',function(){
		$(this).children('a').addClass('hide');
	});
	// 单个图片删除
	$(".content-img-list").on("click",'.content-img-list-item a',function(){
	    	var index = $(this).attr("index");
			imgSrc.splice(index, 1);
			imgFile.splice(index, 1);
			imgName.splice(index, 1);
			var boxId = ".content-img-list";
			addNewContent(boxId);
			if(imgSrc.length<4){//显示上传按钮
				$('.content-img .file').show();
			}
	  });
	//图片上传
	$('#upload').on('change',function(){

		if(imgSrc.length>=2){
			return alert("最多只能上传2张图片");
		}
		var imgSize = this.files[0].size;  //b
		if(imgSize>1024*1024*1){//1M
			return alert("上传图片不能超过1M");
		}
		console.log(this.files[0].type)
		if(this.files[0].type != 'image/png' && this.files[0].type != 'image/jpeg' && this.files[0].type != 'image/gif'){
			return alert("图片上传格式不正确");
		}

		var imgBox = '.content-img-list';
		var fileList = this.files;
		for(var i = 0; i < fileList.length; i++) {
			var imgSrcI = getObjectURL(fileList[i]);
			imgName.push(fileList[i].name);
			imgSrc.push(imgSrcI);
			imgFile.push(fileList[i]);
		}
		addNewContent(imgBox);
		this.value = null;//解决无法上传相同图片的问题
	})

});

//提交请求
function submit_upload(){
    // FormData上传图片
    var formFile = new FormData();
    // formFile.append("type", type);
    // formFile.append("content", content);
    // formFile.append("mobile", mobile);
    // 遍历图片imgFile添加到formFile里面
    $.each(imgFile, function(i, file){
        formFile.append('image'+i, file);
    });
    console.log(imgFile)
     $.ajax({
         url: 'http://127.0.0.1:8000/imageX/uploadimg/',
         type: 'POST',
         data: formFile,
         async: true,
         cache: false,
         contentType: false,
         processData: false,
         // traditional:true,
         dataType:'json',

         success: function (data) {
             alert('上传成功！');
            },
         error: function (data) {
             alert("上传失败");
         }
     })
}
//删除
function removeImg(obj, index) {
	imgSrc.splice(index, 1);
	imgFile.splice(index, 1);
	imgName.splice(index, 1);
	var boxId = ".content-img-list";
	addNewContent(boxId);
}

//图片展示
function addNewContent(obj) {
	// console.log(imgSrc)
	$(obj).html("");
	for(var a = 0; a < imgSrc.length; a++) {
		var oldBox = $(obj).html();
		$(obj).html(oldBox +
		 '<div class="col-md-4 col-xs-6 work content-img-list-item"><img class="img-responsive" src="' + imgSrc[a] +
		  '" alt=""><a index="'+a+'" class="hide delete-btn"><i class="ico-delete"></i>delete</a></div>');
	}
}

//建立一個可存取到該file的url
function getObjectURL(file) {
	var url = null ;
	if (window.createObjectURL!=undefined) { // basic
		url = window.createObjectURL(file) ;
	} else if (window.URL!=undefined) { // mozilla(firefox)
		url = window.URL.createObjectURL(file) ;
	} else if (window.webkitURL!=undefined) { // webkit or chrome
		url = window.webkitURL.createObjectURL(file) ;
	}
	return url ;
}