jQuery(function($) {
    var switcher = $('#currency_switcher');
    switcher.find('select[name=currency]').change(function(event) {
        switcher.submit();
    });
    switcher.find('input[type=submit]').hide();
});
