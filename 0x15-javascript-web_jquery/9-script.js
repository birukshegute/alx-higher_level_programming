$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $hello = $('div#hello');

  function hi () {
    return $.get({
      url: url,
      dataType: 'json'
    });
  }

  hi().then((res) => {
    $hello.text(res.hello);
  });
});
