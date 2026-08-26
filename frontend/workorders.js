function createWorkOrder() {

    const orderId = document.getElementById("orderId").value;
    const product = document.getElementById("product").value;
    const quantity = document.getElementById("quantity").value;
    const status = document.getElementById("status").value;

    const table = document.getElementById("workOrderTable");

    const row = table.insertRow();

    row.insertCell(0).innerHTML = orderId;
    row.insertCell(1).innerHTML = product;
    row.insertCell(2).innerHTML = quantity;
    row.insertCell(3).innerHTML = status;
}
