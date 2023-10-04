

//login.js


$(document).ready(function(){
    $("#submit").click(function(){
        let data = {
            "username": $("#username").val(),
            "password" : $("#password").val(),
            "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val()
        }
        $.ajax({
            url: "/login/",
            type:"POST",
            data: data, 
            success: function(response){
                alert("Connexion réussi!")
            }
        })
    })
});
