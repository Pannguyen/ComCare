

// navbar.js

$(document).ready(function () {
    $.ajax({
        url: '/get_user_info/',  
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.username) {
                $('.user-info').text('Bonjour, ' + response.username);
            }
        },
        error: function (error) {
            console.log('Erreur lors de la récupération des informations de l\'utilisateur :', error);
        }
    });
});


