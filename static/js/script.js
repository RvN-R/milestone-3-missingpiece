/* JQuery for Materialize Components Navbar, 
Mobile Side Navbar, Select, Collapsible*/
$(document).ready(function () {
  $('.sidenav').sidenav({
    edge: "right"
  });
  $('select').formSelect();
  $('.collapsible').collapsible();
});


function validateMaterializeSelect() {
  let classValid = {
    "border-bottom": "1px solid green",
    "box-shadow": "0 1px 0 0 green"
  };
  let classInvalid = {
    "border-bottom": "1px solid red",
    "box-shadow": "0 1px 0 0 red"
  };
  if ($("select.validate").prop("required")) {
    $("select.validate").css({
      "display": "block",
      "height": "0",
      "padding": "0",
      "width": "0",
      "position": "absolute"
    });
  }
  $(".select-wrapper input.select-dropdown").on("focusin", function () {
    if ($(this).val() == 'Choose your Category') $(this).css(classInvalid);
    else $(this).css(classValid);
  })
}

setTimeout(() => validateMaterializeSelect(), 1000);

