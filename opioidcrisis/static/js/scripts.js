function searchTable() {
    var filter = searchBox.value.toUpperCase();
    for (var rowI = 0; rowI < trs.length; rowI++) {
        var tds = trs[rowI].getElementsByTagName("td");
        trs[rowI].style.display = "none";
        for (var cellI = 0; cellI < tds.length; cellI++) {
            if (tds[cellI].innerHTML.toUpperCase().indexOf(filter) > -1) {
                trs[rowI].style.display = "";
                continue;
            }
        }
    }
}

const searchBox = document.getElementById('search');
const table = document.getElementById("table");
const trs = table.tBodies[0].getElementsByTagName("tr");

searchBox.addEventListener('keyup', searchTable);


function searchDrugs() {
    var filter = event.target.value.toUpperCase();
    var rows = document.querySelector("#drugsTable tbody").rows;

    for (var i = 0; i < rows.length; i++) {
        var firstCol = rows[i].cells[0].textContent.toUpperCase(); // name
        var secondCol = rows[i].cells[1].textContent.toUpperCase(); // is opiate
        if (firstCol.indexOf(filter) > -1 || secondCol.indexOf(filter) > -1) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
}

document.querySelector('#searchDrugs').addEventListener('keyup', filterTable, false);