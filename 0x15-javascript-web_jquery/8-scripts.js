const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $List = $('ul#list_movies');

$.ajax({
  url: url,
  dataType: 'json'
}).done((data) => {
  const movies = data.results;

  for (let i = 0; i < movies.length; ++i) {
    const Title_list = movies[i].title;
    const element = `<li>${Title_list}`;
    $List.append(element);
  }
});
