function getData() {
  // alert("1");
  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");

  $.ajax({

      url: "/booking_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#myTable tr:gt(0)").remove();
        for(var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#myTable").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].bk_id+'</td><td>'+response[i].bk_user_name+'</td><td>'+response[i].bk_user_email+'</td><td>'+response[i].bk_seller_name+'</td><td>'+response[i].bk_seller_email+'</td><td>'+response[i].bk_amount+'</td></tr>');
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

function getRowsUpdate() {
  $("#myTable tr").click(function() {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      // var lclName = currentRow.find("td:eq(2)").text();
      // alert(lclName);
      // $("#txtName1").val(lclName);
      $("#edit_id").val(lclID);

      $("#edit_modal").modal('show');

  });
}
