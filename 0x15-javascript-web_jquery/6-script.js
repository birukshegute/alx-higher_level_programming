const $header = $('header');
const $updateHeader = $('div#update_header');

$updateHeader.on('click', () => {
  $header.text('New Header!!!');
});
