function addTable() {
    const tableContainer = document.getElementById("table-container");
    var newTable = document.createElement("table");
    newTable.id = "newTable";

    // Add a table head and first four rows
    var headRow = document.createElement("tr");
    headRow.innerHTML = `<th>SI. No.</th><th> Account No.</th><th>Date of last transaction</th><th>Deposit</th><th>Withdrawal</th><th>Balance</th><th>SMS System alert generated (Y/N)</th><th>.system generated receipt  provided (Y/N)</th><th> 1st page entry of new passbook obtain KYC and initial deposit printed (Y/N)</th>`;
    newTable.appendChild(headRow);

    for (var i = 0; i < 3; i++) {
        var row = document.createElement("tr");
      
        row.innerHTML = `<td>${i+1}</td><td><input type="text" /></td><td><input type="date" /></td><td><input type="text" /></td><td><input type="text" /></td><td><input type="text" /></td><td><input type="text" /></td><td><input type="checkbox" /></td><td><input type="checkbox" /></td>`;
    
        newTable.appendChild(row);
    }

    // Insert the new table after the existing table
    tableContainer.appendChild(newTable);
}
var rowCount = 1; // Initialize row counter

function addRow() {
    var tableBody = document.getElementById("deliveryTable").getElementsByTagName('tbody')[0];
    var newRow = document.createElement('tr');
    newRow.setAttribute("id", "row" + rowCount);

    var cell = document.createElement('td');
    cell.innerHTML = `<select name="checkDeliveryStatus">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                      </select>
                      <input type="text" name="checkDeliveryStatusComments" placeholder="Article no">
                      <p>Date of receipt</p><input type="date" name="dateofreceipt">
                      <p>Date of Delivery</p><input type="date" name="dateofdelivery">`;

    newRow.appendChild(cell);
    tableBody.appendChild(newRow);

    rowCount++; // Increment row counter
}
       