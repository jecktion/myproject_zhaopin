/*--indexi.html----------------------------------------------------------------------------------------------*/
//公司和职位切换
function  choice(){
	$('#tab_comp').click(function(event) {
		$('.ui-autocomplete-input').attr({
			name: 'company',
		});
		$(this).addClass('active');
		$(this).removeClass('disabled');
		$(this).siblings().removeClass('active');

	});
	$('#tab_pos').click(function(event) {
		$('.ui-autocomplete-input').attr({
			name: 'position',
		});
		$(this).addClass('active');
		$(this).removeClass('disabled');
		$(this).siblings().removeClass('active');
	});
}
//学历选择
function contShow(){
	$('#order .edu ').click(function(){
		$(this).find('.edu_ul').toggleClass('hidden');
		
	})
	$('#order .edu').find('li').click(function(){

		var dataEdu = $(this).find('a').attr('data-edu');
		var eduVal = $(this).parents('.text').find('.edu_val').val();
		if (dataEdu == "e01"){
			$(this).parents('.text').find('.edu_val').val('不');
			$(this).parents('.text').find('span').text('不限');
			$(this).parents('.edu_ul').hide();
		}
		if (dataEdu == "e02"){
			$(this).parents('.text').find('.edu_val').val('大专');
			$(this).parents('.text').find('span').text('大专');
			$(this).parents('.edu_ul').hide();
		}
		if (dataEdu == "e03"){
			$(this).parents('.text').find('.edu_val').val('本科');
			$(this).parents('.text').find('span').text('本科');
			$(this).parents('.edu_ul').hide();
		}
		if (dataEdu == "e04"){
			$(this).parents('.text').find('.edu_val').val('硕士');
			$(this).parents('.text').find('span').text('硕士');
			$(this).parents('.edu_ul').hide();
		}
		if (dataEdu == "e05"){
			$(this).parents('.text').find('.edu_val').val('博士');
			$(this).parents('.text').find('span').text('博士');
			$(this).parents('.edu_ul').hide();
		}
		console.log(dataEdu,eduVal,$(this).parents('.edu'),$(this).parents('.text').find('span').text())
	})
		

}
//判断路径
function urlPan(){
	var urlstr = location.href;  
	if (urlstr.indexOf('company') > 0){
		console.log(urlstr.indexOf('company'))
		$('.ui-autocomplete-input').attr({
			name: 'company',
		});
		$('#tab_comp').addClass('active');
		$('#tab_comp').removeClass('disabled');
		$('#tab_comp').siblings().removeClass('active');
	}
}

/*--indexi.html----------------------------------------------------------------------------------------------*/