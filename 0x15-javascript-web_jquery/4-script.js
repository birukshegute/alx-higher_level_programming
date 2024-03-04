const $header = $('header');
const $divRedHeader = $('DIV#toggle_header');

$divRedHeader.on('click', () => {
  const Class = $header.attr('class');

  if (Class === 'green') {
    $header.toggleClass(`${currentClass} red`);
  }

  if (Class === 'red') {
    $header.toggleClass(`${currentClass} green`);
  }
});
