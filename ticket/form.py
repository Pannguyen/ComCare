from django import forms  
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class CreationTicketForm(forms.Form):
    titre = forms.CharField(label = "Titre du ticket", max_length = 255)
    description = forms.CharField(label = "desciption")

    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("titre",css_class = ""),
            Column("description",css_class = ""),

        ), 
        Submit('',"envoyer", css_class = "")
        
    )

