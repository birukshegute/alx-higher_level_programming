const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $Div = $('div#character');

$.ajax({
  url: url,
  dataType: 'json'
}).done((data) => {
  $Div.text(data.name);
});
