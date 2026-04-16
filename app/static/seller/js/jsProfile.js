
  $(document).on("click", "#btn_update", function () {

      if ($("#txtName").val().trim().length < 1) {
        alert("Please Enter Name");
        $("#txtName").focus();
        return false;
      }

      if ($("#txtEmail").val().trim().length < 1) {
        alert("Please Enter Email");
        $("#txtEmail").focus();
        return false;
      }

      if ($("#txtMobileNo").val().trim().length < 1) {
        alert("Please Enter Mobile Number");
        $("#txtMobileNo").focus();
        return false;
      }

      if ($("#txtMobileNo").val().trim().length < 10) {
        alert("Please Enter 10 Digits Mobile Number");
        $("#txtMobileNo").focus();
        return false;
      }

      if ($("#txtPassword").val().trim().length < 1) {
        alert("Please Enter Password");
        $("#txtPassword").focus();
        return false;
      }


    var formData = new FormData()
    formData.append("txtName", $("#txtName").val());
    formData.append("txtEmail", $("#txtEmail").val());
    formData.append("txtPassword", $("#txtPassword").val());
    formData.append("txtMobileNo", $("#txtMobileNo").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("id", $("#edit_id").val());
    formData.append("action", "update");

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/profile_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Profile Details Updated Succesfully");
        location.reload();
        // table.ajax.reload();
        $("#edit_modal").modal('hide');
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        $("#btn_update").attr("disabled", false);
      },
    });
  });


function getData() {

  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");

  $.ajax({

      url: "/profile_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // console.log(response.ad_name);
        // let lclJSON = JSON.parse(response);
        $("#txtName").val(response[0].s_name);
        $("#txtEmail").val(response[0].s_email);
        $("#txtMobileNo").val(response[0].s_mobile);
        $("#txtPassword").val(response[0].s_password);
        $("#edit_id").val(response[0].s_id);
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });

}
getData();