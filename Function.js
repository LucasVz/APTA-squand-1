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
/* Clientes */
$(document).ready(function(){
    $('.slick').slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 1000,
    });
  });

/*Portifólio */
$('.center').slick({
  centerMode: true,
  vertical:true,
  centerPadding: '0px',
  slidesToShow: 1,
  responsive: [
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerMode: false,
        centerPadding: '40px',
        slidesToShow: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 1
      }
    }
  ]
});
	



