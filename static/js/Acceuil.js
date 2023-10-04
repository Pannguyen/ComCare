$(document).ready(function () {
	$(".ticket").click(function () {
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
				etat.append("<h1>" + response["ticket"][5] + "</h1>");
				let date = $(".Date");
				date.empty();
				date.append("<h3>" + response["ticket"][2] + "</h3>");
				let createur = $(".createur");
				createur.empty();
				createur.append("<h3>" + response["ticket"][4] + "</h3>");
			},
		});
	});

	$("#submitnewticketform").click(function () {
		let data = {
			"titre": $("#titre").val(),
			"description": $("#description").val(),
			"csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val(),
		};
		$.ajax({
			url: "/creerTicket/",
			type: "POST",
			data: data,
			success: function (response) {
				alert("Ticket a créé avec succesc");
			},
		});
	});
});
