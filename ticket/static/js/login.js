

//login.js


$(document).ready(function () {
    $("#submit").click(function () {
        if ($("#username").val() == "") {
            alert("Veuillez entrer un nom d'utilisateur.");
            return;
        }
        if ($("#password").val() == "") {
            alert("Veuillez entrer un mot de passe.");
            return;
        }
        let data = {
            "username": $("#username").val(),
            "password": $("#password").val(),
            "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val()
        }
        $.ajax({
            url: "/loginme/",
            type: "POST",
            data: data,
            success: function (response) {
            }
        })
    })
});
