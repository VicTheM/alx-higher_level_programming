// This script fetches and prints how to say “Hello” depending on the language

$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();

    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang,
      (data) => {
        $('DIV#hello').text(data.hello);
      });
  });
});
