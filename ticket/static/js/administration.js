$(document).ready(function () {

    $("#submitnew").click(function () {

        //     <form>
        //     <h2>Nouvel utilisateur</h2>
        //     <div class="input-name input_label">
        //         <label for="username">Nom d'utilisateur:</label>
        //         <input type="text" name="username" id="username" required>
        //     </div>
        //     <div class="input-email input_label">
        //         <label for="email">Adresse email:</label>
        //         <input type="email" name="email" id="email" required>
        //     </div>
        //     <div class="input-first_name input_label">
        //         <label for="first_name">Prénom:</label>
        //         <input type="text" name="first_name" id="first_name">
        //     </div>
        //     <div class="input-last_name input_label">
        //         <label for="last_name">Nom:</label>
        //         <input type="text" name="last_name" id="last_name">
        //     </div>
        //     <div class="input-password input_label">
        //         <label for="password">Mot de passe:</label>
        //         <input type="password" name="password" id="password" required>
        //     </div>
        //     <div class="input-password input_label">
        //         <label for="password">Confirmer le mot de passe:</label>
        //         <input type="password" name="password_confirm" id="password" required>
        //     </div>
        //     <div class="input-button input_label">
        //         <button id="submitnew" type="button">Créer</button>
        //         <button type="reset">Effacer</button>
        //     </div>
        // </form>
        if ($("#username").val() == "") {
            alert("Veuillez entrer un nom d'utilisateur.");
            return;
        }
        if ($("#email").val() == "") {
            alert("Veuillez entrer une adresse email.");
            return;
        }
        if ($("#first_name").val() == "") {
            alert("Veuillez entrer un prénom.");
            return;
        }
        if ($("#last_name").val() == "") {
            alert("Veuillez entrer un nom.");
            return;
        }
        if ($("#password").val() == "") {
            alert("Veuillez entrer un mot de passe.");
            return;
        }
        if ($("#password").val() != $("#password_confirm").val()) {
            console.log($("#password").val());
            console.log($("#password_confirm").val());
            alert("Les mots de passe ne correspondent pas.");
            return;
        }
        let data = {
            "username": $("#username").val(),
            "email": $("#email").val(),
            "first_name": $("#first_name").val(),
            "last_name": $("#last_name").val(),
            "password": $("#password").val(),
            "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val(),
        };
        $.ajax({
            url: "/administration/creerUtilisateur/",
            type: "POST",
            data: data,
            success: function (response) {
                alert("Utilisateur créé.");
                $("#username").val("");
                $("#email").val("");
                $("#first_name").val("");
                $("#last_name").val("");
                $("#password").val("");
                $("#password_confirm").val("");
            },
        });

    });

});