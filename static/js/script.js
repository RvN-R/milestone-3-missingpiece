/* JQuery for Materialize Navbar and Mobile Side Navbar*/
$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('.martinaudo_col').hide();  
  });

  /* Jquery used to open and close Loudspeaker Product Name */
  // $("#loudspeaker_brand_name").click(function(){
  //   $(".loudspeaker_brand_martinaudio").hide();
  // });
  
  $("#loudspeaker_brand_name").click(function(){
    $(".martinaudo_col").show();
  });
