function addTable() {
    const tableContainer = document.getElementById("table-container");
    var newTable = document.createElement("table");
    newTable.id = "newTable";

    // Add a table head and first four rows
    var headRow = document.createElement("tr");
    headRow.innerHTML = `<th>SI. No.</th><th> Account No.</th><th> Scheme-type.</th><th>Date of last transaction</th><th>Deposit</th><th>Withdrawal</th><th>Balance</th><th>SMS System alert generated (Y/N)</th><th>.system generated receipt  provided (Y/N)</th><th> 1st page entry of new passbook obtain KYC and initial deposit printed (Y/N)</th>`;
    newTable.appendChild(headRow);

    for (var i = 0; i < 3; i++) {
        var row = document.createElement("tr");
      
        row.innerHTML = `<td>${i+1}</td><td><input type="text" /> <td><select name="scheme-type">
        <option value="scheme1">scheme1</option>
        <option value="scheme2">scheme2</option>
    </select></td></td><td><input type="date" /></td><td><input type="text" /></td><td><input type="text" /></td><td><input type="text" /></td><td><input type="text" /></td><td><input type="checkbox" /></td><td><input type="checkbox" /></td>`;
    
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
       
var rowCount = 1; // Initialize row counter

function addRow1() {
    var tableBody = document.getElementById("deliveryTable1").getElementsByTagName('tbody')[0];
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
var rowCount = 1; // Initialize row counter

function addRow2() {
    var tableBody = document.getElementById("invoices").getElementsByTagName('tbody')[0];
    var newRow = document.createElement('tr');
    newRow.setAttribute("id", "row" + rowCount);

    var cell = document.createElement('td');
    cell.innerHTML = ` <input type="text" name="invoicestamp" placeholder="invoice">
    <input type="text" name="inventory" placeholder="Comments">`;

    newRow.appendChild(cell);
    tableBody.appendChild(newRow);

    rowCount++; // Increment row counter
}   
var rowCount = 1; // Initialize row counter

function addRow3() {
    var tableBody = document.getElementById("bo-account").getElementsByTagName('tbody')[0];
    var newRow = document.createElement('tr');
    newRow.setAttribute("id", "row" + rowCount);

    var cell = document.createElement('td');
    cell.innerHTML = ` <input type="date" name="dateofaccount" placeholder="date">
    <p>BO SLIP</p><input type="number" name="boslip">
    <p>BO ACCOUNT</p> <input type="number" name="boaccount">`;

    newRow.appendChild(cell);
    tableBody.appendChild(newRow);

    rowCount++; // Increment row counter
}   
var rowCount = 1; // Initialize row counter



function addRow4() {
    var tableBody = document.getElementById("vp/cod").getElementsByTagName('tbody')[0];
    var newRow = document.createElement('tr');
    newRow.setAttribute("id", "row" + rowCount);

    var cell = document.createElement('td');
    cell.innerHTML = ` <p>(i).Article No.</p><input type="number" name="articleNumber" placeholder="Article no">
    <p>Article Issued DATE:</p><input type="date" name="articleIssuedDate"
        placeholder="Article Issued Date">
    <p>Article received DATE</p><input type="date" name="articleReceivedDate"
        placeholder="Article received date">
    <p>Article Delivered DATE:</p><input type="date" name="articleDeliveredDate"
        placeholder="Article Delivered Date">
    <p>VPMO isssued DATE:</p><input type="date" name="VPMOIssuedDate"
        placeholder="VPMO isssued Date">
    <p>(ii).</p> <select name="VPMOIssuedComments">
        <option value="Yes">Yes</option>
        <option value="No">No</option>
    </select>`;

    newRow.appendChild(cell);
    tableBody.appendChild(newRow);

    rowCount++; // Increment row counter
}
var rowCount = 1; // Initialize row counter



function addRow5() {
    var tableBody = document.getElementById("AO").getElementsByTagName('tbody')[0];
    var newRow = document.createElement('tr');
    newRow.setAttribute("id", "row" + rowCount);

    var cell = document.createElement('td');
    cell.innerHTML = ` <input type="number" name="accountnumber" placeholder="accountnumber-ao">
    <select name="allschemes">
        <option value="scheme1">scheme1</option>
        <option value="scheme2">scheme2</option>
    </select>`;

    newRow.appendChild(cell);
    tableBody.appendChild(newRow);

    rowCount++; // Increment row counter
}
function addTable1() {
    const tableContainer = document.getElementsByClassName("table-container1")[0];
    var newTable = document.createElement("table");
    newTable.id = "newTable";

    // Add a table head and first four rows
    var headRow = document.createElement("tr");
    headRow.innerHTML = `<th colspan="3">BOOK NO:</th>
    <th colspan="3">FROM(receipt issued since last visit):</th>
    <th colspan="3">TO(receipt issued since last visit):</th>
    <th colspan="3">BLANK RECEIPT:</th>`;
    newTable.appendChild(headRow);

    var Row1 = document.createElement("tr");
    Row1.innerHTML = ` <td  colspan="3"><input type="text" name="SB28_book_no" /></td>

    <!-- FROM Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- TO Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- BLANK RECEIPT Section -->
    <td colspan="3"><input type="text" name="SB28_blank_receipt" /></td>`;
    newTable.appendChild(Row1);
    var Row2 = document.createElement("tr");
    Row2.innerHTML = `<td colspan="3"></td>

    <!-- FROM Sub-columns -->
    <td><input type="text" name="SB28_receipt_no_from" /></td>
    <td><input type="date" name="SB28_date_from" /></td>
    <td><input type="number" name="SB28_amount_from" /></td>

    <!-- TO Sub-columns -->
    <td><input type="text" name="SB28_receipt_no_to" /></td>
    <td><input type="date" name="SB28_date_to" /></td>
    <td><input type="number" name="SB28_amount_to" /></td>

    <!-- Empty cells for Blank Receipt -->
    <td colspan="3"></td>`;
    newTable.appendChild(Row2);

    // Insert the new table after the existing table
    tableContainer.appendChild(newTable);
}
function addTable2() {
    const tableContainer = document.getElementsByClassName("table-container2")[0];
    var newTable = document.createElement("table");
    newTable.id = "newTable";

    // Add a table head and first four rows
    var headRow = document.createElement("tr");
    headRow.innerHTML = `<th colspan="3">BOOK NO:</th>
    <th colspan="3">FROM(receipt issued since last visit):</th>
    <th colspan="3">TO(receipt issued since last visit):</th>
    <th colspan="3">BLANK RECEIPT:</th>`;
    newTable.appendChild(headRow);

    var Row1 = document.createElement("tr");
    Row1.innerHTML = ` <td  colspan="3"><input type="text" name="SB28_book_no" /></td>

    <!-- FROM Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- TO Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- BLANK RECEIPT Section -->
    <td colspan="3"><input type="text" name="SB28_blank_receipt" /></td>`;
    newTable.appendChild(Row1);
    var Row2 = document.createElement("tr");
    Row2.innerHTML = `<td colspan="3"></td>

    <!-- FROM Sub-columns -->
    <td><input type="text" name="SB28_receipt_no_from" /></td>
    <td><input type="date" name="SB28_date_from" /></td>
    <td><input type="number" name="SB28_amount_from" /></td>

    <!-- TO Sub-columns -->
    <td><input type="text" name="SB28_receipt_no_to" /></td>
    <td><input type="date" name="SB28_date_to" /></td>
    <td><input type="number" name="SB28_amount_to" /></td>

    <!-- Empty cells for Blank Receipt -->
    <td colspan="3"></td>`;
    newTable.appendChild(Row2);

    // Insert the new table after the existing table
    tableContainer.appendChild(newTable);
}
function addTable3() {
    const tableContainer = document.getElementsByClassName("table-container3")[0];
    var newTable = document.createElement("table");
    newTable.id = "newTable";

    // Add a table head and first four rows
    var headRow = document.createElement("tr");
    headRow.innerHTML = `<th colspan="3">BOOK NO:</th>
    <th colspan="3">FROM(receipt issued since last visit):</th>
    <th colspan="3">TO(receipt issued since last visit):</th>
    <th colspan="3">BLANK RECEIPT:</th>`;
    newTable.appendChild(headRow);

    var Row1 = document.createElement("tr");
    Row1.innerHTML = ` <td  colspan="3"><input type="text" name="SB28_book_no" /></td>

    <!-- FROM Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- TO Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- BLANK RECEIPT Section -->
    <td colspan="3"><input type="text" name="SB28_blank_receipt" /></td>`;
    newTable.appendChild(Row1);
    var Row2 = document.createElement("tr");
    Row2.innerHTML = `<td colspan="3"></td>

    <!-- FROM Sub-columns -->
    <td><input type="text" name="SB28_receipt_no_from" /></td>
    <td><input type="date" name="SB28_date_from" /></td>
    <td><input type="number" name="SB28_amount_from" /></td>

    <!-- TO Sub-columns -->
    <td><input type="text" name="SB28_receipt_no_to" /></td>
    <td><input type="date" name="SB28_date_to" /></td>
    <td><input type="number" name="SB28_amount_to" /></td>

    <!-- Empty cells for Blank Receipt -->
    <td colspan="3"></td>`;
    newTable.appendChild(Row2);

    // Insert the new table after the existing table
    tableContainer.appendChild(newTable);
}
function addTable4() {
    const tableContainer = document.getElementsByClassName("container")[0];
    var newTable = document.createElement("table");
    newTable.id = "newTable";
    // Set display to block

    // Add a table head and first four rows
    var headRow = document.createElement("tr");
    headRow.innerHTML = `<td>
    <label for="question2">(v) Check whether the unused SB-26 receipts are intact and run in consecutive
        order</label>
</td><td><input type="text" name="acquittance_comments" placeholder="Comments"></td>`;
    newTable.appendChild(headRow);

    var Row1 = document.createElement("tr");
    Row1.innerHTML = ` <td>
    <label for="question2">(v) Check whether the unused SB-26 receipts are intact and run in consecutive
        order</label>
</td>
<td><input type="text" name="unused_receipts_comments" placeholder="Comments"></td>`;
    newTable.appendChild(Row1);
    var Row2 = document.createElement("tr");
    Row2.innerHTML = ` <td>
    <label for="question3">(vi) Check whether reference number of new account is entered on the original SB-26
        receipts.</label>
</td>
<td><input type="text" name="reference_number_comments" placeholder="Comments"></td>`;
    newTable.appendChild(Row2);

    // Insert a line break
    tableContainer.appendChild(document.createElement("br"));

    // Insert the new table after the line break
    tableContainer.appendChild(newTable);
}

