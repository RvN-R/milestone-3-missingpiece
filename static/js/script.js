/* JQuery for Materialize Navbar and Mobile Side Navbar*/
$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $(".hide_loudspeaker_brand_row").hide();
    $(".hide_loudspeaker_product_row").hide();
    $(".hide_mixer_brand_row").hide();
    $(".hide_mixer_product_row").hide();
    $(".hide_mic_brand_row").hide();
    $(".hide_mic_product_row").hide();

  });
/* Loudspeaker Brand Inventory Form Function*/
$("#loudspeaker_no_btn").click(function(){
  $("#loudspeaker_brand").val("Don't Hold Stock"); 
  $("#loudspeaker_product").val("N/A");
  $("#loudspeaker_product_qty").val(0);
  $(".loudspeaker_brand_row").show(1000);
  $(".loudspeaker_product_row").show(1000);

});
/* Loudspeaker Product Inventory Form Function */
$("#loudspeaker_yes_btn").click(function(){
  $("#loudspeaker_brand").val(""); 
  $("#loudspeaker_product").val("");
  $("#loudspeaker_product_qty").val("");
  $(".loudspeaker_brand_row").show(1000);
  $(".loudspeaker_product_row").show(1000);
});
/*Mixer Brand Inventory Form Function*/
$("#mixer_no_btn").click(function(){
  $("#mixer_brand").val("Don't Hold Stock"); 
  $("#mixer_product").val("N/A");
  $("#mixer_product_qty").val(0);
  $(".mixer_brand_row").show(1000);
  $(".mixer_product_row").show(1000);

});
/* Mixer Product Inventory Form Function */
$("#mixer_yes_btn").click(function(){
  $("#mixer_brand").val(""); 
  $("#mixer_product").val("");
  $("#mixer_product_qty").val("");
  $(".mixer_brand_row").show(1000);
  $(".mixer_product_row").show(1000);
});
/*Microphone Brand Inventory Form Function*/
$("#mic_no_btn").click(function(){
  $("#microphone_brand").val("Don't Hold Stock"); 
  $("#microphone_product").val("N/A");
  $("#microphone_product_qty").val(0);
  $(".mic_brand_row").show(1000);
  $(".mic_product_row").show(1000);

});
/* Microphone Product Inventory Form Function */
$("#mic_yes_btn").click(function(){
  $("#microphone_brand").val(""); 
  $("#microphone_product").val("");
  $("#microphone_product_qty").val("");
  $(".mic_brand_row").show(1000);
  $(".mic_product_row").show(1000);
});
