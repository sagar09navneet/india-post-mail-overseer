var rowCount = 1;
function addTable() {
    const tableContainer = document.getElementById("table-container");
    var newTable = document.createElement("table");
    newTable.id = "newTable";

    // Add a table head and first four rows
    var headRow = document.createElement("tr");
    headRow.innerHTML = `<th>SI. No.</th><th> Account No.${rowCount}</th><th> Scheme-type.${rowCount}</th><th>Date of last transaction${rowCount}</th><th>Deposit${rowCount}</th><th>Withdrawal${rowCount}</th><th>Balance${rowCount}</th><th>SMS System alert generated (Y/N)${rowCount}</th><th>.system generated receipt  provided (Y/N)${rowCount}</th><th> 1st page entry of new passbook obtain KYC and initial deposit printed (Y/N)</th>${rowCount}`;
    newTable.appendChild(headRow);

    for (var i = 0; i < 3; i++) {
        var row = document.createElement("tr");
      
        row.innerHTML = `<td>${i+1}</td><td><input type="text" /> <td><select name="scheme-type${rowCount}">
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
    var rowCount = document.getElementById("deliveryTable").getElementsByTagName('tr').length; // Assuming you have at least one row as header

    // Setting a unique ID for the row based on the rowCount
    newRow.setAttribute("id", "row" + rowCount);

    var cell = document.createElement('td');

    // Updated input names to include the rowCount to ensure uniqueness
    cell.innerHTML = `<select name="check_delivery_status_acc${rowCount}">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                      </select>
                      <input type="text" name="check_delivery_status_comments_acc${rowCount}" placeholder="Article no">
                      <p>Date of receipt</p><input type="date" name="date_of_receipt_acc${rowCount}">
                      <p>Date of Delivery</p><input type="date" name="date_of_delivery_acc${rowCount}">`;

    newRow.appendChild(cell);
    tableBody.appendChild(newRow);
}

       



var rowCount = 1
function addRow1() {
    var tableBody = document.getElementById("deliveryTable1").getElementsByTagName('tbody')[0];
    var newRow = document.createElement('tr');
    var rowCount = document.getElementById("deliveryTable1").getElementsByTagName('tr').length; // Assuming you have at least one row as header

    // Setting a unique ID for the row based on the rowCount
    newRow.setAttribute("id", "row" + rowCount);

    var cell = document.createElement('td');

    // Updated input names to include the rowCount to ensure uniqueness
    cell.innerHTML = `<select name="check_delivery_status_ord${rowCount}">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                      </select>
                      <input type="text" name="check_delivery_status_comments_ord${rowCount}" placeholder="Article no">
                      <p>Date of receipt</p><input type="date" name="date_of_receipt_ord${rowCount}">
                      <p>Date of Delivery</p><input type="date" name="date_of_delivery_ord${rowCount}">`;

    newRow.appendChild(cell);
    tableBody.appendChild(newRow);
}



var rowCount = 1; // Initialize row counter

function addRow2() {
    var tableBody = document.getElementById("invoices").getElementsByTagName('tbody')[0];
    var newRow = document.createElement('tr');
    newRow.setAttribute("id", "row" + rowCount);

    var cell = document.createElement('td');
    cell.innerHTML = ` <input type="text" name="invoice_stamp${rowCount}" placeholder="invoice">
    <input type="text" name="inventory${rowCount}" placeholder="Comments">`;

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
    cell.innerHTML = ` <input type="date" name="date_of_account${rowCount}" placeholder="date">
    <p>BO SLIP</p><input type="number" name="bo_slip${rowCount}">
    <p>BO ACCOUNT</p> <input type="number" name="bo_account${rowCount}">`;

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
    cell.innerHTML = ` <p>(i).Article No.</p><input type="number" name="article_number${rowCount}" placeholder="Article no">
    <p>Article Issued DATE:</p><input type="date" name="article_issued_date${rowCount}"
        placeholder="Article Issued Date">
    <p>Article received DATE</p><input type="date" name="article_received_date${rowCount}"
        placeholder="Article received date">
    <p>Article Delivered DATE:</p><input type="date" name="article_delivered_date${rowCount}"
        placeholder="Article Delivered Date">
    <p>VPMO isssued DATE:</p><input type="date" name="VPMO_issued_date${rowCount}"
        placeholder="VPMO isssued Date">
    <p>(ii).</p> <select name="VPMO_issued_comments${rowCount}">
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
    cell.innerHTML = ` <input type="number" name="account_number_ao${rowCount}" placeholder="accountnumber-ao">
    <select name="all_schemes${rowCount}">
        <option value="scheme1">scheme1</option>
        <option value="scheme2">scheme2</option>
    </select>`;

    newRow.appendChild(cell);
    tableBody.appendChild(newRow);

    rowCount++; // Increment row counter
}


var rowCount = 1; 

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
    Row1.innerHTML = ` <td  colspan="3"><input type="text" name="book_no_SB26${rowCount}" /></td>

    <!-- FROM Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- TO Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- BLANK RECEIPT Section -->
    <td colspan="3"><input type="text" name="blank_receipt_SB26${rowCount}" /></td>`;
    newTable.appendChild(Row1);
    var Row2 = document.createElement("tr");
    Row2.innerHTML = `<td colspan="3"></td>

    <!-- FROM Sub-columns -->
    <td><input type="text" name="receipt_no_from_SB26${rowCount}" /></td>
    <td><input type="date" name="date_from_SB26${rowCount}" /></td>
    <td><input type="number" name="amount_from_SB26${rowCount}" /></td>

    <!-- TO Sub-columns -->
    <td><input type="text" name="receipt_no_to_SB26${rowCount}" /></td>
    <td><input type="date" name="date_to_SB26${rowCount}" /></td>
    <td><input type="number" name="amount_to_SB26${rowCount}" /></td>

    <!-- Empty cells for Blank Receipt -->
    <td colspan="3"></td>`;
    newTable.appendChild(Row2);
    rowCount++; // Increment row counter
    // Insert the new table after the existing table

    tableContainer.appendChild(newTable);
}

var rowCount = 1; 

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
    Row1.innerHTML = ` <td  colspan="3"><input type="text" name="book_no_SB28${rowCount}" /></td>

    <!-- FROM Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- TO Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- BLANK RECEIPT Section -->
    <td colspan="3"><input type="text" name="blank_receipt_SB28${rowCount}" /></td>`;
    newTable.appendChild(Row1);
    var Row2 = document.createElement("tr");
    Row2.innerHTML = `<td colspan="3"></td>

    <!-- FROM Sub-columns -->
    <td><input type="text" name="receipt_no_from_SB28${rowCount}" /></td>
    <td><input type="date" name="date_from_SB28${rowCount}" /></td>
    <td><input type="number" name="amount_from_SB28${rowCount}" /></td>

    <!-- TO Sub-columns -->
    <td><input type="text" name="receipt_no_to_SB28${rowCount}" /></td>
    <td><input type="date" name="date_to_SB28${rowCount}" /></td>
    <td><input type="number" name="SB28_amount_to${rowCount}" /></td>

    <!-- Empty cells for Blank Receipt -->
    <td colspan="3"></td>`;
    newTable.appendChild(Row2);

    // Insert the new table after the existing table
    tableContainer.appendChild(newTable);
}



var rowCount = 1; 

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
    Row1.innerHTML = ` <td  colspan="3"><input type="text" name="book_no_MS87${rowCount}" /></td>

    <!-- FROM Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- TO Section -->
    <th>Receipt No</th>
    <th>Date</th>
    <th>Amount</th>

    <!-- BLANK RECEIPT Section -->
    <td colspan="3"><input type="text" name="blank_receipt_MS87${rowCount}" /></td>`;
    newTable.appendChild(Row1);
    var Row2 = document.createElement("tr");
    Row2.innerHTML = `<td colspan="3"></td>

    <!-- FROM Sub-columns -->
    <td><input type="text" name="receipt_no_from_MS87${rowCount}" /></td>
    <td><input type="date" name="date_from_MS87${rowCount}" /></td>
    <td><input type="number" name="amount_from_MS87${rowCount}" /></td>

    <!-- TO Sub-columns -->
    <td><input type="text" name="receipt_no_to_MS87${rowCount}" /></td>
    <td><input type="date" name="date_to_MS87${rowCount}" /></td>
    <td><input type="number" name="amount_to_MS87${rowCount}" /></td>

    <!-- Empty cells for Blank Receipt -->
    <td colspan="3"></td>`;
    newTable.appendChild(Row2);

    // Insert the new table after the existing table
    tableContainer.appendChild(newTable);
}


var rowCount = 1; 
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
</td><td><input type="text" name="acquittance_comments${rowCount}" placeholder="Comments"></td>`;
    newTable.appendChild(headRow);

    var Row1 = document.createElement("tr");
    Row1.innerHTML = ` <td>
    <label for="question2">(v) Check whether the unused SB-26 receipts are intact and run in consecutive
        order</label>
</td>
<td><input type="text" name="unused_receipts_comments${rowCount}" placeholder="Comments"></td>`;
    newTable.appendChild(Row1);
    var Row2 = document.createElement("tr");
    Row2.innerHTML = ` <td>
    <label for="question3">(vi) Check whether reference number of new account is entered on the original SB-26
        receipts.</label>
</td>
<td><input type="text" name="reference_number_comments${rowCount}" placeholder="Comments"></td>`;
    newTable.appendChild(Row2);

    // Insert a line break
    tableContainer.appendChild(document.createElement("br"));

    // Insert the new table after the line break
    tableContainer.appendChild(newTable);
}

