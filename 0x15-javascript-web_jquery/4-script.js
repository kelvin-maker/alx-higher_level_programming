$('DIV#toggle_header').click(function () {
  if ($('HEADER').hasClass('red')) {
    $('HEADER').removeClass('red');
    $('HEADER').addClass('green');
  } else if ($('HEADER').hasClass('green')) {
    $('HEADER').removeClass('green');
    $('HEADER').addClass('red');
  }
});
