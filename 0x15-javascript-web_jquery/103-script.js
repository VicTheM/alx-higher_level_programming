// This script fetches and prints how to say “Hello” depending on the language

function sayHello () {
  const lang = $('INPUT#language_code').val();

  $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang,
    (data) => {
      $('DIV#hello').text(data.hello);
    });
}

$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    sayHello();
  });

  $('INPUT#language_code').on('keydown', (event) => {
    if (event.which === 13) {
      sayHello();
    }
  });
});
