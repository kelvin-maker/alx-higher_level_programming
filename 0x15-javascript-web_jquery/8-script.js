$.get('https://swapi.co/api/films/?format=json', function (data) {
  $.each(data.results, function (index, value) {
    $('<li>' + value.title + '</li>').appendTo('UL#list_movies');
  });
});
