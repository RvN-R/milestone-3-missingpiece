/* JQuery for Materialize Navbar and Mobile Side Navbar*/
$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('.loudspeaker_product_name_col').hide();  
  });

  /* Jquery used to open and close Loudspeaker Product Name */
  $("#close").click(function(){
    $(".loudspeaker_product_name_col").hide();
  });
  
  $("#open").click(function(){
    $(".loudspeaker_product_name_col").show();
  });
