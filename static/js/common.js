$(document).ready(function() {
    $('#search-dropdown li a').on('click', function (e) {
        e.preventDefault();
        $('#search-toggle-btn').html(e.target.innerText + ' <span class="caret"></span>');
    });

    $('#search-form').on('submit', function (e) {
        e.preventDefault();
        value = $('#search-item').val();

        if (value === "") return;
        
        alert(value);
    });
});