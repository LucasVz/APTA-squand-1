function abrir1(){
	document.getElementById('popup-1').style.display = 'block';
}

function abrir2(){
	document.getElementById('popup-2').style.display = 'block';
}

function abrir3(){
	document.getElementById('popup-3').style.display = 'block';
}

function abrir4(){
	document.getElementById('popup-4').style.display = 'block';
}


function fechar(){
	if(getElementById = 'popup-1')
		document.getElementById('popup-1').style.display =  'none';
	if(getElementById = 'popup-2')
		document.getElementById('popup-2').style.display =  'none';	
	if(getElementById = 'popup-3')
		document.getElementById('popup-3').style.display =  'none';
	if(getElementById = 'popup-4')
		document.getElementById('popup-4').style.display =  'none';
}

$(document).ready(function(){
    $('.slick').slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 1000,
    });
  });