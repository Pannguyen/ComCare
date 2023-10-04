$(document).ready(function(){

    $("#msg_submit").click(function(){
        let data = {
            "msg": $("#message").val(),
        };
        $.ajax({
            url: "/CreateTicket/",
            type: "POST",
            data: data,
            success: function (response) {
                get_message()
            },
        });
    });

    function get_message(){
        $.ajax({
            url: "/GetTicketMessages/",
            type: "GET",
            success: function (response) {
                let list_messages = $("#list_msg");
                list_messages.empty();
                let html = "";
                $.each(response['messages'], function (index, message) {
                    html += '<div>';
                    html += '<h4>' + message['user'] + '</h4>';
                    html += '<p>' + message['msg'] + '</p>';
                    html += '<p>' + message['date'] + '</p>';
                    html += '</div>';
                    list_messages.append(html);
                });
            },
        });
    }
});