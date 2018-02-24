/*公共导航部分--------------------------------------*/
//顶部导航鼠标经过出现内容
function topNav(){
	var oWrapper = $('#scroll-wrap');
	var oHeader = $('.header ');
	var bg_white = oWrapper.find('.bg-white');
	var nav_item = oWrapper.find('[data-subNav]');
	var sub_nav = oWrapper.find('.layout-header-nav-child');
	var subNav_wrapper = sub_nav.find('.layout-header-nav-child-list');
	var lw = $('.layout-header-nav-child-list li').width();
	var timer = null;

	nav_item.hover(function () {
		clearTimeout(timer);
		hoverChange();
		var getVal = $(this).attr('data-subNav');
		var subNav_cur = $('.layout-header-nav-child-list[data-link='+getVal+']');
		var t = subNav_cur.find('li').length;
		var uw = lw * t /2;
		subNav_cur.css('margin-left',-uw);
		var cur_imgs = subNav_cur.find('a');
		goodsShow(subNav_cur);
		showImg(cur_imgs);
		nav_theme('hover');

	}, function () {
		timer = setTimeout(function () {
			outChange();
			nav_theme('out');
		}, 100);
	})


	sub_nav.hover(function () {
		clearTimeout(timer);
			nav_theme('hover');
		}, function () {
			timer = setTimeout(function () {
			outChange();
			nav_theme('out');
		}, 100);
	});

	function hoverChange() {
		bg_white.fadeIn('fast');
		sub_nav.animate({height: 139});
	};

	function outChange() {
		bg_white.fadeOut('slow');
		sub_nav.animate({height: 0});
	};

	// 当前商品容器显示
	function goodsShow(subNav_cur) {
		subNav_wrapper.hide();
		subNav_cur.show();
	};

	// 小列表显示
	function showImg(aImg) {
		var num = 0;
		var timer = null;

		aImg.css({opacity: 0, marginLeft: 30});
		for (var i = 0; i < aImg.length; i++) {
			aImg.eq(i).animate({marginLeft: 0, opacity: 1}, 500);
			if (i === aImg.length - 1) {
				clearInterval(timer);
			}
		}

		// 图片移入移出
		aImg.hover(function () {
			$(this).css({opacity: 1}).parent('.layout-header-nav-child-item').siblings().find('.layout-header-nav-child-link').css({opacity: 0.6});
		}, function () {
			aImg.css({opacity: 1});
		});
	};

	function nav_theme(method) {
		if (method === 'hover') {
			if (oWrapper.hasClass('theme-white')) {
				oWrapper.addClass('theme-nav');
			}
		} else {
			oWrapper.removeClass('theme-nav');
		}
	};


}//顶部导航鼠标经过出现内容 E

function topLogin(){
	// 登录图片鼠标经过
	$('#layoutHeaderUser').mouseover(function(){
		$('.layout-user-downmenu').show();
	}).mouseout(function() {
		$('.layout-user-downmenu').hide();
	});
}
// 公共返回顶部
function backTop(){
	$(window).scroll(function(){
	var dTop = $(document).scrollTop();
	var fTop = $('.layout-header .navbar').height();
	if(dTop >fTop){
		$('.layout-magnet').show();
	}else{
		$('.layout-magnet').hide();
	}
	});
	$(".layout-magnet").click(function(){
		$("html").animate({"scrollTop": "0px"},500); //IE,FF
		$("body").animate({"scrollTop": "0px"},500); //Webkit
	});
} 

//登录之后显示用户名
function gUserLogin(){
	var gUser = $('#layoutHeaderUser .gusername').text();
	if(gUser != ''){
		$('.g-user').hide();
	}else{
		$('.g-user').show()
	}
}
//购物车显示实际购买的总数量
function serviceCartNum(){
	var serviceCartNum = $('.serviceCartNum').length;
	var i = 0;
	var cartNumSum = 0;
	for(var i = 0;i<serviceCartNum;i++){
		var cartNum = Number($('.serviceCartNum').eq(i).text())
		cartNumSum += cartNum;
	}
	$('.layout-header-service-cart-num').text(cartNumSum)
}

/*---------------------------------------------------*/ 

/*首页部分-------------------------------------------*/
// 首页侧导航鼠标经过出现内容
function leftNav(){
	$('#homeCategory li').mouseover(function(){
		$(this).find('.home-category-child').show();
	}).mouseout(function(){
		$(this).find('.home-category-child').hide();
	})
}

/*---------------------------------------------------*/ 

/*全部商品部分---------------------------------------*/
function comPro(){
	$(".gl-item").mouseover(function(){
		$(this).find('.compare-btn-list').css('display','block');
	});
	$(".gl-item").mouseout(function(){
		$(this).find('.compare-btn-list').css('display','none');
	});

}

/*---------------------------------------------------*/ 

/*产品详情页部分-------------------------------------*/
function  detaNav(){
	$('#detailFast ul li').click(function(){
		var t = $(this).index();

		$('#detailFast ul li').addClass('current').siblings().removeClass('current');
		$('.detail-content div').eq(t).addClass('current').siblings().removeClass('current');
	})
	$(window).scroll(function(){
		var dt = $('#detail').offset().top;
		var dTop = $(document).scrollTop();
		if(dTop >= dt){
			$('#detailFast').addClass('float-nav');
		}else{
			$('#detailFast').removeClass('float-nav');
		}
	})
} 
// 数量增加减少
function addMin(){
	// 减少
	$('.vm-minus').click(function(){
		var n=$('#J_quantity').val();
		
		var num=parseInt(n)-1;
		if(num<=1){ 
			$('.vm-minus').addClass('disabled');
			$('.vm-plus').removeClass('disabled');
			$(this).next().val(1);
		}else{
			$('.goodsinfo').text('');
			$('.vm-minus').removeClass('disabled');
			$('.vm-plus').removeClass('disabled');
			$(this).next().val(num);
		
		}

	})
	// //input丧失焦点事件
	// $('#J_quantity').blur(function(){
	// 	var n=$('#J_quantity').val();
	// 	if(n<1){
	// 		$('#J_quantity').val(1);
	// 		$('.vm-minus').addClass('disabled');
	// 		$('.vm-plus').removeClass('disabled');
	// 	}else if(n>1 && n<20){
	// 		$('.vm-minus').removeClass('disabled');
	// 		$('.vm-plus').removeClass('disabled');
	// 	}else if(n == 20){
	// 		$('.vm-plus').addClass('disabled');
	// 	}else if(n>20){
	// 		$('#J_quantity').val(20);
	// 		$('.vm-minus').removeClass('disabled');
	// 		return;
	// 	}
	// })
	//增加
	$('.vm-plus').click(function(){
		var n=$('#J_quantity').val();
		var num=parseInt(n)+1;
		//判断库存
		var gstore = parseInt($('input[name=gstore]').val());
		if(num <= gstore){
			$('.vm-minus').removeClass('disabled');
			$('.vm-plus').removeClass('disabled');
		}else{
			num = gstore;
			$('.goodsinfo').text('库存不足,请重新选择!');
			$('.vm-plus').addClass('disabled');
		}
		$(this).prev().val(parseInt(num));
		


	})
}// 数量增加减少E

function topFix(){
	$(function(){
	$('#scroll-wrap .navbar').removeClass('navbar-fixed-top');
})

}
/*---------------------------------------------------*/ 
/*移动端特效-----------------------------------------*/
function appTopNav(){
	$(window).scroll(function(){
		var dTop = $(document).scrollTop();
		if(dTop>0){
			$('#J_listFilter').addClass('fixed');
		}else{
			$('#J_listFilter').removeClass('fixed');
		}
	})
}
/*---------------------------------------------------*/ 
function allSelect(){
	var aee = false;
	// 全选
	$('.JSelectAll input[name=tselectall]').click(function(){
		var dCheck = $('input[name = mzckpro]');
		if(aee){
			for (i in dCheck){
				dCheck[i].checked=false;
			}
			aee = false;
		}else{
			for (i in dCheck){
				dCheck[i].checked=true;
			}
			aee = true;
		}
	})
	// 底部全选
	$('.JSelectAll input[name=fselectall]').click(function(){
		var dCheck = $('input[name = mzckpro]');
		if(aee){
			for (i in dCheck){
				dCheck[i].checked=false;
			}
			aee = false;
		}else{
			for (i in dCheck){
				dCheck[i].checked=true;
			}
			aee = true;
		}
	})

}

//选中商品结算传递到订单页面
function loadTotal(){

	var ids = [];
	//获取所有选择的商品
	var list = $("table.cart-merchant-body div.mz-checkbox").filter(".checked");
	for(var i=0;i<list.length;i++){
		ids.push($(list[i]).attr('pid'));
	}
	return ids;
}


/*登录页面----------------------------------------*/ 
function nLogin(){
	//   提交
	var unameOk=false;
	var passOk=false;
	var repassOk=false;
	var phoneOk=false;
	var emailOk=false;
	//获取焦点事件
	$('input[name=username]').focus(function(){
		//添加颜色
		$('#cycode-box').addClass('btn-focus');
		$('.passwd-box').removeClass('btn-focus');
		})
	$('input[name=password]').focus(function(){
		$('#cycode-box').removeClass('btn-focus');
		$('.passwd-box').addClass('btn-focus');
	})
	//丧失焦点事件
	$('input[name=username]').blur(function(){
		//获取用户信息进行正则获取
		var v =$(this).val();
		var reg=/^\w{4,32}$/;
		//判断如果为true则通过
		if(reg.test(v)){
			$('#cycode-box').removeClass('btn-error');
			$('#unameVerify').addClass('hidden');
			unameOk=true;
		}else{
		$('#cycode-box').addClass('btn-error');
			$('#unameVerify').removeClass('hidden');
			$('#unameVerify').html("请输入格式正确的用户名")
			unameOk=false;
		}
	})
	//丧失焦点事件
	$('input[name=passwd]').blur(function(){
		//获取用户信息
		var v =$(this).val();
		var reg=/^\w{6,18}$/;
		//判断如果为true则通过
		if(reg.test(v)){
			$('.passwd-box').removeClass('btn-error');
			$('#passVerify').addClass('hidden');
			passOk=true;
		}else{
		$('.passwd-box').addClass('btn-error');
			$('#passVerify').removeClass('hidden');
			$('#passVerify').html("请输入格式正确的密码")
			passOk=false;
		}
	})

	//重复密码丧失焦点事件
	$('input[name=repasswd]').blur(function(){
		//获取重复密码
		var v =$(this).val();
		var reg=/^\w{6,32}$/;
		//判断如果为true则通过
		if(reg.test(v)){
			$('.repass-box').removeClass('btn-error');
			$('#repassVerify').addClass('hidden');
			repassOk=true;
		}else{
		$('.repass-box').addClass('btn-error');
			$('#repassVerify').removeClass('hidden');
			$('#repassVerify').html("请输入格式正确的密码")
			repassOk=false;
		}
	})
	//手机号丧失焦点事件
	$('input[name=phone]').blur(function(){
		//获取手机号
		var v =$(this).val();
		var reg=/^\w{6,16}$/;
		//判断如果为true则通过
		if(reg.test(v)){
			$('.phone-box').removeClass('btn-error');
			$('#phoneVerify').addClass('hidden');
			phoneOk=true;
		}else{
		$('.phone-box').addClass('btn-error');
			$('#phoneVerify').removeClass('hidden');
			$('#phoneVerify').html("请输入格式正确的手机号")
			phoneOk=false;
		}
	})
	//邮箱丧失焦点事件
	$('input[name=email]').blur(function(){
		//获取邮箱
		var v =$(this).val();
		var reg=/^\w+@\w+\.(com|cn|org|net)$/;
		//判断如果为true则通过
		if(reg.test(v)){
			$('.email-box').removeClass('btn-error');
			$('#emailVerify').addClass('hidden');
			emailOk=true;
		}else{
		$('.email-box').addClass('btn-error');
			$('#emailVerify').removeClass('hidden');
			$('#emailVerify').html("请输入格式正确的邮箱")
			emailOk=false;
		}
	})
}

/*---------------------------------------------------*/ 

/*订单详情展示页-----------------------------*/ 

//订单展开收起
function navOpenClose(){
	$('.order-main .type-contain .orderItem .trHead ').click(function() {
		$(this).next('.list-box').toggleClass('hiddens');
	});
}
//按钮点击订单状态修改
function offStatChange(){
	//发送ajax请求确认收货
	function oddStaAjax(orstatus,orid){
		$.ajax({
			url: "/orderoffsta",
			type: 'GET',
			dataType: 'json',
			data:{'orstatus':orstatus,'orid':orid},
			error:function() {
				alert("ajax加载失败！");
			},
		})
	}
	//发送ajax请求取消订单
	function celStaAjax(orstatus,orid){
		$.ajax({
			url: "/ordercelsta",
			type: 'GET',
			dataType: 'json',
			data:{'orstatus':orstatus,'orid':orid},
			error:function() {
				alert("ajax加载失败！");
			},
		})
	}

	//确认收货
	$('#O_verify').click(function(){
		var vFlag = confirm('请确定是否已收到商品,一旦确定收货,状态不可修改?');
		if(!vFlag){
			return false;
		}
		//确认收货提示弹框
		else{
			var orstatus = parseInt($(this).parents('tbody').find('.ordstatediv').attr('ods'));
			orstatus = 2;
			// $('.ostate').text('已收货');
			var orid = parseInt($(this).parents('tbody').find('.orderNumber').text());
			// $('.ordstatediv').text(orstatus);
			oddStaAjax(orstatus,orid);
		}
	});

	//取消订单
	$('.orderItem #O_cancel').click(function(){
		var cFlag = confirm('确定要取消订单吗?');
		if(!cFlag){
			return false;
		}
		//取消订单提示弹框
		else{
			var orstatus = parseInt($(this).parents('tbody').find('.ordstatediv').attr('ods'));
			orstatus = 3;
			// $('.ostate').text('已收货');
			var orid = parseInt($(this).parents('tbody').find('.orderNumber').text());
			// $('.ordstatediv').text(orstatus);
			celStaAjax(orstatus,orid);
		}	
	});
}
/*---------------------------------------------------*/ 

/*列表页----------------------------------------*/ 
function sortChange(){
	var urlstr = location.href;  
	$('.filter .filter-order a').each(function(){
		var orturl = $(this).attr('href');
		if(urlstr.indexOf(orturl) != -1){
			$(this).addClass('active');
			$(this).siblings().removeClass('active');
		}
	})
	

}

/*---------------------------------------------------*/ 
