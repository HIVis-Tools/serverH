// A $( document ).ready() block.
$( document ).ready(function() {
        $("#id_protein_choice").change(function(){
        $("#id_ref_string").hide();
        });
	$("#id_protein_choice").val("other").change(function(){
	$("#id_ref_string").show();	
	});
});


