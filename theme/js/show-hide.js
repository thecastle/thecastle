$(document).ready(function() {
  $('div.outline-2> div').hide();
  $('div.outline-2> h2').click(function() {
  $(this).siblings('div').toggle();
		return false;
  }).siblings('div').hide();




});
