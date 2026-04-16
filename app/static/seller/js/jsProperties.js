$("#btn_add").click(function() {

  if($("#filePhoto").val() == "") {
    alert("Please Select Normal Photo");
    $("#filePhoto").focus();
    return false;
  }

  if($("#filePhoto1").val() == "") {
    alert("Please Select 360 Degree Photo");
    $("#filePhoto1").focus();
    return false;
  }

  if($("#txtName").val() == "") {
    alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }

  if($("#selCategory").val() == "" || $("#selCategory").val() == "Please Select Category") {
    alert("Please Select Category");
    $("#selCategory").focus();
    return false;
  }

  if($("#txtProperty").val() == "" || $("#txtProperty").val() == "Please Select Property") {
    alert("Please Select Property Type");
    $("#txtProperty").focus();
    return false;
  }

  if($("#selCity").val() == "" || $("#selCity").val() == "Please Select City") {
    alert("Please Select City");
    $("#selCity").focus();
    return false;
  }

  if($("#txtPlace").val() == "") {
    alert("Please Enter your Place");
    $("#txtPlace").focus();
    return false;
  }

  if($("#txtFee").val() == "") {
    alert("Please Enter Fee");
    $("#txtFee").focus();
    return false;
  }

  if($("#txtDate").val() == "") {
    alert("Please Enter current Date");
    $("#txtDate").focus();
    return false;
  }

  if($("#txtMobileNo").val() == "") {
    alert("Please Enter your Mobile number");
    $("#txtMobileNo").focus();
    return false;
  }

    var formData = new FormData();

    let lclFileNormal = document.getElementById("filePhoto");
    lclFileNormal1 = lclFileNormal.files[0];
    formData.append("filePhoto", lclFileNormal1);

    let lclFile360 = document.getElementById("filePhoto1");
    lclFile3601 = lclFile360.files[0];
    formData.append("filePhoto1", lclFile3601);
  
    formData.append("txtName", $("#txtName").val());
    formData.append("selCategory", $("#selCategory").val());
    formData.append("txtProperty", $("#txtProperty").val());
    formData.append("selCity", $("#selCity").val());
    formData.append("txtPlace", $("#txtPlace").val());
    formData.append("txtFee", $("#txtFee").val());
    formData.append("txtDesc", $("#txtDesc").val());
    formData.append("txtDate", $("#txtDate").val());
    formData.append("txtMobileNo", $("#txtMobileNo").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "add");


  $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_add").attr("disabled", true);
      },
      url: "/seller_properties/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {

        alert("Property Added Successfully");
        location.reload();
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

function getCategory() {
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");

  $.ajax({

      url: "/web_category/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#selCategory").html('<option value="">Please Select Category</option>');
        $("#selCategory1").html('<option value="">Please Select Category</option>');
        for(var i = 0; i < response.length; i++) {
          $("#selCategory").append('<option value="'+response[i].ca_name+'">'+response[i].ca_name+'</option>');
          $("#selCategory1").append('<option value="'+response[i].ca_name+'">'+response[i].ca_name+'</option>');
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });

}

getCategory();

function getData() {
    var formData = new FormData();
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "getData");

    $.ajax({

      url: "/seller_properties/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#tableData").empty();
        for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].pr_id+'</td><td>'+response[i].pr_seller_name+'</td><td>'+response[i].pr_category+'</td><td>'+response[i].pr_property_type+'</td><td>'+response[i].pr_location+'</td><td>'+response[i].pr_place+'</td><td>'+response[i].pr_fee+'</td><td>'+response[i].pr_desc+'</td><td>'+response[i].pr_date+'</td><td>'+response[i].pr_mobile_no+'</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();"> <i class="fa fa-edit"></i></a><a href="javascript:void(0);" title="Delete" data-toggle="modal" data-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();"> <i class="far fa-trash-alt"></i></a></div></td></tr>');
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {

      },
    });

}

getData();


$("#btn_update").click(function() {

  if($("#txtName1").val() == "") {
    alert("Please Enter Name");
    $("#txtName1").focus();
    return false;
  }

  if($("#selCategory1").val() == "" || $("#selCategory1").val() == "Please Select Category") {
    alert("Please Select Category");
    $("#selCategory1").focus();
    return false;
  }

  if($("#txtProperty1").val() == "" || $("#txtProperty1").val() == "Please Select Property") {
    alert("Please Select Property Type");
    $("#txtProperty1").focus();
    return false;
  }

  if($("#selCity1").val() == "" || $("#selCity1").val() == "Please Select City") {
    alert("Please Select City");
    $("#selCity1").focus();
    return false;
  }

  if($("#txtPlace1").val() == "") {
    alert("Please Enter your Place");
    $("#txtPlace1").focus();
    return false;
  }

  if($("#txtFee1").val() == "") {
    alert("Please Enter Fee");
    $("#txtFee1").focus();
    return false;
  }

  if($("#txtDate1").val() == "") {
    alert("Please Enter current Date");
    $("#txtDate1").focus();
    return false;
  }

  if($("#txtMobileNo1").val() == "") {
    alert("Please Enter your Mobile number");
    $("#txtMobileNo1").focus();
    return false;
  }

    var formData = new FormData();

    let lclFile = document.getElementById("filePhoto");
    lclFile1 = lclFile.files[0];
    formData.append("filePhoto", lclFile1);
  
    formData.append("txtName1", $("#txtName1").val());
    formData.append("selCategory1", $("#selCategory1").val());
    formData.append("txtProperty1", $("#txtProperty1").val());
    formData.append("selCity1", $("#selCity1").val());
    formData.append("txtPlace1", $("#txtPlace1").val());
    formData.append("txtFee1", $("#txtFee1").val());
    formData.append("txtDesc1", $("#txtDesc1").val());
    formData.append("txtDate1", $("#txtDate1").val());
    formData.append("txtMobileNo1", $("#txtMobileNo1").val());
    formData.append("id", $("#edit_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "update");

  $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_add").attr("disabled", true);
      },
      url: "/seller_properties/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {

        alert("Property Updated Successfully");
        location.reload();
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

$(document).on("click", "#btn_delete", function () {

    var formData = new FormData();
    formData.append("id", $("#delete_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "delete")

    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
      },

      url: "/seller_properties/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function () {
        alert("Property Details deleted succesfully");
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
      var lclCategory = currentRow.find("td:eq(3)").text();
      var lclProperty = currentRow.find("td:eq(4)").text();
      var lclCity = currentRow.find("td:eq(5)").text();
      var lclPlace = currentRow.find("td:eq(6)").text();
      var lclFee = currentRow.find("td:eq(7)").text();
      var lclDesc = currentRow.find("td:eq(8)").text();
      var lclDate = currentRow.find("td:eq(9)").text();
      var lclMobile = currentRow.find("td:eq(10)").text();

      $("#txtName1").val(lclName);
      $("#selCategory1").val(lclCategory);
      $("#txtProperty1").val(lclProperty);
      $("#selCity1").val(lclCity);
      $("#txtPlace1").val(lclPlace);
      $("#txtFee1").val(lclFee);
      $("#txtDesc1").val(lclDesc);
      $("#txtDate1").val(lclDate);
      $("#txtMobileNo1").val(lclMobile);
      $("#edit_id").val(lclID);

      $("#edit_modal").modal('show');

  });
}


function getRowsDelete() {
  $("#tableData tr").click(function() {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      $("#delete_id").val(lclID);
      $("#delete_modal").modal('show');

  });
}