let ETAT_CHOICE = {
	"C": ["Créé", "#00FF00"],
	"A": ["En attente", "#0000AA"],
	"E": ["En cours", "#444444"],
	"T": ["Terminé", "#FF0000"],
};

$(document).ready(function () {
	$("#submitnewticketform").click(function () {
		let data = {
			"titre": $("#titre").val(),
			"description": $("#description").val(),
			"csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val(),
			"categories": $("#categorie").val().join(","),
		};
		$.ajax({
			url: "/creerTicket/",
			type: "POST",
			data: data,
			success: function (response) {
				GetTickets();
			},
		});
		$("#titre").val("");
		$("#description").val("");
	});

	$("#submitfilter").click(function () {
		GetTickets();
	});

	$(".Nouveauticket").find("button").click(function () {
		$(".formnewticket").removeClass("hiden");
		$(".detail").addClass("hiden");
	});
	GetTickets();
	$(".formnewticket").removeClass("hiden");
	$(".detail").addClass("hiden");
});

function GetTickets() {
	data = {
		"categories": $("#categoriefilter").val().join(","),
	};
	$.ajax({
		url: "/gettickets/",
		type: "GET",
		data: data,
		success: function (response) {
			let tickets = response["tickets"];
			let list_tickets = $(".ListeTicket");
			list_tickets.empty();
			$.each(tickets, function (index, ticket) {
				html = '<div class="ticket"><input type="hidden" name="pk" value="';
				html += ticket[6]; // pk
				html += '"><h3 class="Elementticket">';
				html += ticket[0]; // titre
				html += '</h3><div class="flex-row-sbw"><p class="Elementticket">';
				html += ticket[2]; // date
				html += '</p><p class="Elementticket">';
				html += ticket[5]; // etat
				html += "</p></div></div>";
				list_tickets.append(html);
			});
			$(".ticket").click(function () {
				$(".formnewticket").addClass("hiden");
				$(".detail").removeClass("hiden");
				let id = $(this).find("input[name=pk]").val();
				$.ajax({
					url: "/getticketdetail/" + id + "/",
					type: "GET",
					success: function (response) {
						let titre = $(".Titre");
						titre.empty();
						titre.append("<h1>" + response["ticket"][0] + "</h1>");
						let description = $(".Description");
						description.empty();
						description.append("<h3>" + response["ticket"][1] + "</h3>");
						let etat = $(".Etat");
						etat.empty();
						etat.append(
							'<h1 style="color:' + ETAT_CHOICE[response["ticket"][5]][1] +
							';">' + ETAT_CHOICE[response["ticket"][5]][0] + "</h1>",
						);
						let date = $(".Date");
						date.empty();
						date.append("<h3>" + response["ticket"][2] + "</h3>");
						let createur = $(".createur");
						createur.empty();
						createur.append("<h3>" + response["ticket"][4] + "</h3>");
						$("#msg_submit").off("click");
						$("#msg_submit").click(function () {
							let data = {
								"msg": $("#message").val(),
								"csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]")
									.val(),
							};
							$.ajax({
								url: "/CreateTicket/" + id + "/",
								type: "POST",
								data: data,
								success: function (response) {
									get_message(id);
									$("#message").val("");
								},
							});
						});
						get_message(id);
					},
				});
			});
		},
	});
}

function get_message(id) {
	$.ajax({
		url: "/GetTicketMessages/" + id + "/",
		type: "GET",
		success: function (response) {
			let list_messages = $("#list_msg");
			list_messages.empty();
			$.each(response["messages"], function (index, message) {
				let html = "";
				html += "<div>";
				html += "<h4>" + message[2] + "</h4>";
				html += "<p>" + message[0] + "</p>";
				html += "<p>" + message[1] + "</p>";
				html += "</div>";
				list_messages.append(html);
			});
		},
	});
}
