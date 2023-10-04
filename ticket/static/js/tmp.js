$(document).ready(function(){

    $("#msg_submit").click(function(){
        let data = {
            "msg": $("#message").val(),
            "csrfmiddlewaretoken" : $("input[name=csrfmiddlewaretoken]").val()
        };
        $.ajax({
            url: "/CreateTicket/1/",
            type: "POST",
            data: data,
            success: function (response) {
                get_message()
            },
        });
    });

    function get_message(){
        $.ajax({
            url: "/GetTicketMessages/1/",
            type: "GET",
            success: function (response) {
                let list_messages = $("#list_msg");
                list_messages.empty();
                $.each(response['messages'], function (index, message) {
                    let html = "";
                    html += '<div>';
                    html += '<h4>' + message[2] + '</h4>';
                    html += '<p>' + message[0] + '</p>';
                    html += '<p>' + message[1] + '</p>';
                    html += '</div>';
                    list_messages.append(html);
                });
            },
        });
    }
});