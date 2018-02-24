(function(){
	var calc = function(){
		//获取当前文档
		var html = document.documentElement;
		// 判断 当前文档宽度 大于 750 那么变量就是 750,否则就是当前文档实际宽度
		var clientWidthValue = html.clientWidth > 750 ? 750 : html.clientWidth;
		//设置当前文档的字体大小
		html.style.fontSize = 20*(clientWidthValue/375)+'px';

	}
	calc();
	//绑定事件,当浏览器的大小发生改变时
	window.addEventListener('resize',calc);
})();