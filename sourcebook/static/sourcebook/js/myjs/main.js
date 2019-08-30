//ulの設定
$(function () {
    //.accordionの中のp要素がクリックされたら
	$('.accordion p').click(function(){
		//クリックされた.accordion1の中のp要素に隣接するul要素が開いたり閉じたりする。
		$(this).next('ul').slideToggle();
	});
});
