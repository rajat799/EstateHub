function getData() {
    const formData = new FormData();
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "getData");
  
    $.ajax({
  
        url: "/orders_details_admin/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
          // Clear all rows except header from #myTable
          $("#myTable tbody").empty();
          for(var i = 0; i < response.length; i++) {
            var j = i + 1;
            $("#myTable tbody").append('<tr><td>' + j + '</td><td style="display: none;">' + response[i].or_id + '</td><td>' + response[i].or_date + '</td><td>' + response[i].or_name + '</td><td>' + response[i].or_email + '</td><td>' + response[i].or_mobile + '</td><td>' + response[i].or_transaction_id + '</td><td>' + response[i].or_address + '</td><td>' + response[i].or_total_amount + '</td><td><button type="button" onClick="viewProducts(' + response[i].or_id + ');" class="btn btn-success">View Products</button></td></tr>');
          }
        },
        error: function (request, error) {
          console.error(error);
        },
        complete: function () {
  
        },
      });
  
  }
  getData()

  function viewProducts(orderID) {

    const formData = new FormData();
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("orderID", orderID);
    $.ajax({
        beforeSend: function () {
        },
        url: "/view_products/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            $("#exampleModal").modal('show');
            $("#tableDataProducts tr:gt(0)").remove();
            for (var i = 0; i < response.length; i++) {
                let img = response[i].pp_image.substring(3);
                var j = i + 1;
                $("#tableDataProducts").append('<tr><td>' + j + '</td><td style="display: none;">' + response[i].or_id + '</td><td><img class="" src="' + img + '" alt="" height="100" style="width: 50%;"></td><td>' + response[i].pp_name + '</td><td>' + response[i].pp_category + '</td><td>' + response[i].pp_price + '</td><td>' + response[i].pp_qty + '</td><td>' + response[i].pp_total_amount + '</td></tr>');
            }

        },
        error: function (request, error) {
            console.error(error);
        },
        complete: function () {
        },
    });
}