const $header = $('header');
const $divRedHeader = $('div#red_header');

$divRedHeader.on('click', function () {
  $header.css('color', '#FF0000');
});
