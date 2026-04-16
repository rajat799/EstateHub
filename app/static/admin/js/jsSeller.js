function alphaOnly(event) {
  var key = event.which ? event.which : event.keyCode;
  return (
    (key >= 65 && key <= 90) ||
    key == 8 ||
    (event.charCode >= 97 && event.charCode <= 122) ||
    event.charCode == 32
  );
}

function validateEmail(paramEmailID) {
  var filter = /^[0-9a-z.]+\@[a-z0-9]+\.[a-zA-z0-9]{2,4}$/;
  
  if (filter.test(paramEmailID)) {
    return true;
  } else {
    return false;
  }
}

function isNumberKey(evt) {
  var charCode = (evt.which) ? evt.which : event.keyCode;
  if (charCode > 31 && (charCode < 48 || charCode > 57)) {
      return false;
  }
  return true;
}

$("#btn_add").click(function (e) {
  //verification
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

  if(!validateEmail($("#txtEmail").val())) {
     alert("Please Enter valid Email");
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

  if ($("#txtAddress").val().trim().length < 1) {
    alert("Please Enter Address");
    $("#txtAddress").focus();
    return false;
  }

  //append data
  var formData = new FormData();
  formData.append("txtName", $("#txtName").val());
  formData.append("txtEmail", $("#txtEmail").val());
  formData.append("txtMobileNo", $("#txtMobileNo").val());
  formData.append("txtAddress", $("#txtAddress").val());
  formData.append("txtPassword", $("#txtPassword").val());
  formData.append("selRole", $("#selRole").val());
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "add");

  // var table = $("#tableData").DataTable();

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_add").attr("disabled", true);
    },
    url: "/admin_seller/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {
      // alert(result);
      if(result.trim() == "10") {
        alert("Email already Exist, Please Check and Add");
      } else {
        alert("Seller Added Successfully");
        location.reload();
        table.ajax.reload();
        $("#add_modal").modal('hide');
      }
      
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      $("#btn_add").attr("disabled", false);
    },
  });
});
// var sl_no = 0;
// ADD Testimnials data Table (DONE)
function getAdminData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");

  $.ajax({

      url: "/admin_seller/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#tableData tr:gt(0)").remove();
        for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].s_id+'</td><td>'+response[i].s_name+'</td><td>'+response[i].s_email+'</td><td>'+response[i].s_mobile+'</td><td>'+response[i].s_address+'</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();"><i class="fa fa-edit"></i></a><a href="javascript:void(0);" title="Delete" data-toggle="modal" data-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();"><i class="fas fa-trash-alt"></i></a></div></td></tr>');
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });

}
getAdminData();



  //Edit modal submit click
  $(document).on("click", "#btn_update", function () {

    if ($("#txtName1").val() == "") {
        alert("Please Enter Name");
        $("#txtName1").focus();
        return false;
    }

    if ($("#txtEmail1").val() == "") {
        alert("Please Enter Email");
        $("#txtEmail1").focus();
        return false;
    }

    if ($("#txtMobileNo1").val() == "") {
        alert("Please Enter Mobile Number");
        $("#txtMobileNo1").focus();
        return false;
    }


    if ($("#txtAddress1").val() == "") {
        alert("Please Enter Address");
        $("#txtAddress1").focus();
        return false;
    }

 
    
    let formData = new FormData();
    formData.append("txtName1", $("#txtName1").val());
    formData.append("txtEmail1", $("#txtEmail1").val());
    formData.append("txtMobileNo1", $("#txtMobileNo1").val());
    formData.append("txtAddress1", $("#txtAddress1").val());
    formData.append("selRole1", $("#selRole1").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("id", $("#edit_id").val());
    formData.append("action", "update");

    // var table = $("#tableData").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/admin_seller/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Seller Details Updated Succesfully");
        location.reload();
        table.ajax.reload();
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

  //Delete work step
  $(document).on("click", "#btn_delete", function () {

    var formData = new FormData();
    formData.append("id", $("#delete_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "delete")
    // var table = $("#tableData").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
      },

      url: "/admin_seller/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function () {
        alert("Seller Details deleted succesfully");
        location.reload();
        table.ajax.reload();
        $("#delete_modal").modal('hide');
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        // Reset Form
        //$("#view_field_form")[0].reset();
        $(".close").click();
      },
    });
  });


  function getRowsUpdate() {
  $("#tableData tr").click(function() {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      var lclName = currentRow.find("td:eq(2)").text();
      var lclEmail = currentRow.find("td:eq(3)").text();
      var lclMobile = currentRow.find("td:eq(4)").text();
      var lclAddress = currentRow.find("td:eq(5)").text();
      // alert(lclName);
      $("#txtName1").val(lclName);
      $("#txtMobileNo1").val(lclMobile);
      $("#txtEmail1").val(lclEmail);
      $("#txtAddress1").val(lclAddress);
      $("#edit_id").val(lclID);

      $("#edit_modal").modal('show');

  });
}


function getRowsDelete() {
  $("#tableData tr").click(function() {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      // alert(lclID);
      $("#delete_id").val(lclID);
      $("#delete_modal").modal('show');

  });
}