$("#btn_add").click(function() {

  if($("#filePhoto").val() == "") {
    alert("Please Select Photo");
    $("#filePhoto").focus();
    return false;
  }

  if($("#txtName").val() == "") {
    alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }

  if($("#selCategory").val() == "") {
    alert("Please Select Category");
    $("#selCategory").focus();
    return false;
  }


  if($("#txtPrice").val() == "") {
    alert("Please Enter Price");
    $("#txtPrice").focus();
    return false;
  }

  if($("#txtDate").val() == "") {
    alert("Please Enter current Date");
    $("#txtDate").focus();
    return false;
  }

 

    const formData = new FormData();

    let lclFile = document.getElementById("filePhoto");
    lclFile1 = lclFile.files[0];
    formData.append("filePhoto", lclFile1);
  
    formData.append("txtName", $("#txtName").val());
    formData.append("selCategory", $("#selCategory").val());
    formData.append("txtPrice", $("#txtPrice").val());
    formData.append("txtDesc", $("#txtDesc").val());
    formData.append("txtDate", $("#txtDate").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "add");

  $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_add").attr("disabled", true);
      },
      url: "/product_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {

        alert("Product Added Successfully");
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
function getData() {
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");

  $.ajax({

      url: "/product_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#tableData tr:gt(0)").remove();
        for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].pd_id+'</td><td>'+response[i].pd_name+'</td><td>'+response[i].pd_category+'</td><td>'+response[i].pd_price+'</td><td>'+response[i].pd_desc+'</td><td>'+response[i].pd_date+'</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();"> <i class="fa fa-edit"></i></a><a href="javascript:void(0);" title="Delete" data-toggle="modal" data-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();"> <i class="far fa-trash-alt"></i></a></div></td></tr>');
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

  if($("#selCategory1").val() == "") {
    alert("Please Select Category");
    $("#selCategory1").focus();
    return false;
  }


  if($("#txtPrice1").val() == "") {
    alert("Please Enter Fee");
    $("#txtPrice1").focus();
    return false;
  }

  if($("#txtDate1").val() == "") {
    alert("Please Enter current Date");
    $("#txtDate1").focus();
    return false;
  }

    var formData = new FormData();

    let lclFile = document.getElementById("filePhoto");
    lclFile1 = lclFile.files[0];
    formData.append("filePhoto", lclFile1);
  
    formData.append("txtName1", $("#txtName1").val());
    formData.append("selCategory1", $("#selCategory1").val());
    formData.append("txtPrice1", $("#txtPrice1").val());
    formData.append("txtDesc1", $("#txtDesc1").val());
    formData.append("txtDate1", $("#txtDate1").val());
    formData.append("id", $("#edit_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "update");

    // console.log(typeof(formData));

  $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_add").attr("disabled", true);
      },
      url: "/product_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {

        alert("Product Updated Successfully");
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

      url: "/product_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function () {
        alert("Product Details deleted succesfully");
        location.reload();
        table.ajax.reload();
        $("#delete_modal").modal('hide');
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
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
      var lclPrice = currentRow.find("td:eq(4)").text();
      var lclDesc = currentRow.find("td:eq(5)").text();
      var lclDate = currentRow.find("td:eq(6)").text();

      $("#txtName1").val(lclName);
      $("#selCategory1").val(lclCategory);
      $("#txtPrice1").val(lclPrice);
      $("#txtDesc1").val(lclDesc);
      $("#txtDate1").val(lclDate);
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