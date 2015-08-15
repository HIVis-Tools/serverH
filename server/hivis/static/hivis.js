$(document).ready(function(){
	$("#id_ref_string").hide();

    $('#id_protein_choice').on('change', function() {
	if ( this.value == 'other')
      {
        $("#id_ref_string").show();
      }
      else
      {
        $("#id_ref_string").hide();
      }
    });
});



