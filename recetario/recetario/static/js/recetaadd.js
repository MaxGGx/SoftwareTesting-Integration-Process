// Hide success added to cart
$("#success-alert").hide();
// Hide failed added to cart
$("#failed-alert").hide();

// Show successful added advice
function showAlert() {
    $("#success-alert").fadeTo(2000, 500).slideUp(500, function(){
   $("#success-alert").slideUp(500);
    });   
};
// Show Failed added advice
function showAlert2() {
    $("#failed-alert").fadeTo(2000, 500).slideUp(500, function(){
   $("#failed-alert").slideUp(500);
    });   
};
