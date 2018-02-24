

/*购物车--------------------------------------------*/ 

//选择框操作
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

// 数量增加减少
function cartAddMin(){

	//发送ajax请求
	function doajax(goodsid,gnum){
		$.ajax({
			url: "/cartchanum",
			type: 'GET',
			dataType: 'json',
			data:{'goodsid':goodsid,'goodsnum':gnum},
			error:function() {
				alert("ajax加载失败！");
			},
		})
	}

	var $pList = $('.cart-product');

	//初始商品总和
	var i = 0;
	var fsPrice = 0;
	var fsNum = 0;
	var sPrice = 0;
	//进入购物车时显示的初始值
	while(i<$pList.length){
		//每条数据的数量
		var gnum = Number($pList.eq(i).find('.mz-adder-input').val());
		//底部总商品数量
		fsNum = Number(fsNum)+Number(gnum);
		//所有商品价钱
		var dsPrice =  Number($pList.eq(i).find('.cart-product-price.total').text());
		//每条数据的单价
		var djPrice = parseFloat($pList.eq(i).find('.cart-product-price.dj-price').text());
		//小计
		var sPrice= parseFloat(djPrice)*parseFloat(gnum); 
		$pList.eq(i).find('.cart-product-price.total').text(sPrice+'.00');
		//  小计
		fsPrice += sPrice;

		i++;
		//底部总商品数量
		$('#totalCount').text(fsNum);    

	}

	if ($('#totalCount').text() == ''){
		$('#totalCount').text(0);
	}
	if ($('#totalSelectCount').text() == ''){
		$('#totalSelectCount').text(0);
	}
	if ($('#totalPrice').text() == ''){
		$('#totalPrice').text('0.00');
	}
	//页面底部显示初始值:数量和价钱的
	//加号操作
	$('.mz-adder-add').click(function(){
		var gnum = $(this).prev().find('.mz-adder-input').val();
		gnum ++;
		$(this).prev().find('.mz-adder-input').val(gnum);
		var goodsid = $(this).parents('.cart-product').find('input[name=goodsid]').val();
		doajax(goodsid,gnum);

		//每条数据的单价
		var djPrice = parseFloat($(this).parents('.cart-product').find('.cart-product-price.dj-price').text());
		//小计
		var sPrice= parseFloat(djPrice) * parseFloat(gnum);
		$(this).parents('.cart-product').find('.cart-product-price.total').text(sPrice+'.00');
		//底部总数量
		var fsNum = Number($('#totalCount').text());
		//底部总商品数量
		fsNum++;
		//底部总商品数量
		$('#totalCount').text(fsNum);
		if($(this).parents('.cart-product').find('input[name=mzckpro]').is(':checked')){

			//底部总价钱
			var xjSumPrice = parseFloat( $('#totalPrice').text());
			xjSumPrice += djPrice;
			$('#totalPrice').text(xjSumPrice);

			//底部选中数量
			var sNum = Number($('#totalSelectCount').text());
			sNum ++;
			$('#totalSelectCount').text(sNum);
		}

		if(gnum>1&& gnum<20){ 
			$(this).siblings('.mz-adder-subtract').removeClass('disabled');
			$(this).removeClass('disabled');
		}


	});
	//选中状态下的加号操作

	//减号操作
	$('.mz-adder-subtract ').click(function(){
		var gnum = $(this).next().find('.mz-adder-input').val();
		gnum=gnum-1;
		if(gnum<1){
			gnum = 1;
		}
		$(this).next().find('.mz-adder-input').val(gnum);
		var goodsid = $(this).parents('.cart-product').find('input[name=goodsid]').val();
		doajax(goodsid,gnum);
		//每条数据的单价
		var djPrice = parseFloat($(this).parents('.cart-product').find('.cart-product-price.dj-price').text());
		//小计
		var sPrice= parseFloat(djPrice * gnum);
		$(this).parents('.cart-product').find('.cart-product-price.total').text(sPrice+'.00');
		if(gnum>1){
			//底部总数量
			var fsNum = Number($('#totalCount').text());
			//底部总商品数量
			fsNum--;
			//底部总商品数量
			$('#totalCount').text(fsNum);
		}else{
			var tc = $('.cart-product').length;
			$('#totalCount').text(tc);     
		}


		if (gnum<=1){ 
			gnum =1;
			$(this).addClass('disabled');
			$(this).siblings('.mz-adder-add').removeClass('disabled');
		}else{
			$(this).removeClass('disabled');
			$(this).siblings('.mz-adder-add').removeClass('disabled');
			$(this).next().find('.mz-adder-input').val(gnum);
		}
	});
	//全选
	$('input[name=tselectall]').change(function(){
		var dee = $(this).is(":checked");
		if(dee){
			$('#totalSelectCount').text(Number($('#totalCount').text()));
			$('#totalPrice').text(fsPrice+'.00');
		}else{
			$('#totalSelectCount').text(0);
			$('#totalPrice').text('0.00');
		}
	})

	//底部选中商品数量
	$('input[name=mzckpro]').change(function(){
		var dee = $(this).is(":checked");
		//底部显示被选中数量
		var gnum = Number($(this).parents('.cart-product').find('.mz-adder-input').val());
		var sNum = Number($('#totalSelectCount').text());
		var djPrice = parseFloat($(this).parents('.cart-product').find('.cart-product-price.dj-price').text());
		var xjSumPrice = parseFloat( $('#totalPrice').text());
		// //每条数据的小计
		var xjPrice = parseFloat(djPrice)*parseFloat(gnum);
		$(this).parents('.cart-product').find('.cart-product-price.total').text(xjPrice+'.00');
		//底部商品总和
		if (dee){
			sNum += gnum;
			xjSumPrice += xjPrice;
			$(this).parents('.cart-product').find('.mz-adder-add ').click(function(){
				var gnum = Number($(this).parents('.cart-product').find('.mz-adder-input').val());
				var sNum = Number($('#totalSelectCount').text());
				var djPrice = parseFloat($(this).parents('.cart-product').find('.cart-product-price.dj-price').text());
				var xjSumPrice = parseFloat($('#totalPrice').text());
				gnum ++;
				sNum ++;
				xjSumPrice +=djPrice;
				$('#totalSelectCount').text(sNum);
				$('#totalPrice').text(xjSumPrice+'.00');
			})
			$(this).parents('.cart-product').find('.mz-adder-subtract ').click(function(){
				var gnum = Number($(this).parents('.cart-product').find('.mz-adder-input').val());
				var sNum = Number($('#totalSelectCount').text());
				var djPrice = parseFloat($(this).parents('.cart-product').find('.cart-product-price.dj-price').text());
				var xjSumPrice = parseFloat($('#totalPrice').text());
				gnum --;
				sNum --;
				xjSumPrice -=djPrice;
				
				$('#totalSelectCount').text(sNum);
				$('#totalPrice').text(xjSumPrice+'.00');
			})
		}else{
			sNum -= gnum;
			xjSumPrice -= xjPrice;
		}
		$('#totalSelectCount').text(sNum);
		$('#totalPrice').text(xjSumPrice+'.00');
		// loadTotal();

	})


	$('.cart-col-select .mz-checkbox').click(function(){
		$(this).toggleClass("checked");
		loadTotal();
	})

}// 数量增加减少E 

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

/*---------------------------------------------------*/ 

