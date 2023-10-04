// temporaire.js

$(document).ready(function(){
    $("#submitnewticketform").click(function(){
        let data = {
            "titre": $("#titre").val(),
            "description" : $("#description").val(),
            "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val()
        }
        $.ajax({
            url: "/creerTicket/",
            type:"POST",
            data: data
        })
    })
});