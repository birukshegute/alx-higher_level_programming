const $header = $('header');
const $divRedHeader = $('div#red_header');

$divRedHeader.on('click', function () {
  $header.addClass('red');
});
