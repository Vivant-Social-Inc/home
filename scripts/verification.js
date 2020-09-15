$(document).ready(() => {
  function makeSiteUsable() {
    $("#age-verification").hide();
    $("#age-overlay").css("display", "none");
    $(".navbar").css("visibility", "visible");
  }

  if (sessionStorage.getItem("ageVerification") === "true") {
    makeSiteUsable();
  }

  $("#age-verify-confirm").click(() => {
    makeSiteUsable();
    sessionStorage.setItem("ageVerification", "true");
  });
});
