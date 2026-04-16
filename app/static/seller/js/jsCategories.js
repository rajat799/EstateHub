
    function validateEmail(paramEmailID) {
      var filter = /^[0-9a-z.]+\@[a-z0-9]+\.[a-zA-z0-9]{2,4}$/;
      
      if (filter.test(paramEmailID)) {
        return true;
      } else {
        return false;
      }
    }

    

$("#btn_add").click(function (e) {
  //verification
  if ($("#txtName").val().trim().length < 1) {
    alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }

  var formData = new FormData();
  
  formData.append("txtName", $("#txtName").val());
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "add");


  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_add").attr("disabled", true);
    },
    url: "/category_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {

      alert("category Added Successfully");
      location.reload();
      // table.ajax.reload();
      $("#add_modal").modal('hide');
      
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
$(document).ready(function () {

  getAdminData();

  //Edit modal submit click
  $(document).on("click", "#btn_update", function () {

    if ($("#txtName1").val().trim().length < 1) {
      alert("Please Enter Name");
      $("#txtName11").focus();
      return false;
    }


    var formData = new FormData()
    formData.append("txtName1", $("#txtName1").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("id", $("#edit_id").val());
    formData.append("action", "update");

    // var table = $("#tableData").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/category_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Category Details Updated Succesfully");
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

  //Delete work step
  $(document).on("click", "#btn_delete", function () {

    var formData = new FormData();
    formData.append("id", $("#delete_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "delete");

    // var table = $("#tableData").DataTable();

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
      },

      url: "/category_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function () {
        alert("Category Details deleted succesfully");
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
});

function getAdminData() {

  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");

  $.ajax({

      url: "/category_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#tableData tr:gt(0)").remove();
        for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].ca_id+'</td><td>'+response[i].ca_name+'</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();">Edit </a><a href="javascript:void(0);" title="Delete" data-toggle="modal" data-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();">Delete</a></div></td></tr>');
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });

}

function getRowsUpdate() {
  $("#tableData tr").click(function() {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      var lclName = currentRow.find("td:eq(2)").text();
      // alert(lclName);
      $("#txtName1").val(lclName);
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