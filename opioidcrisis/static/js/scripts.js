function searchPrescribers() {
    var filter = event.target.value.toUpperCase();
    var rows = document.querySelector("#prescribersTable tbody").rows;

    for (var i = 0; i < rows.length; i++) {
        var firstCol = rows[i].cells[0].textContent.toUpperCase(); // name
        var secondCol = rows[i].cells[1].textContent.toUpperCase(); // gender
        var thirdCol = rows[i].cells[2].textContent.toUpperCase(); // credentials
        var fourthCol = rows[i].cells[3].textContent.toUpperCase(); // credentials
        if (firstCol.indexOf(filter) > -1 || secondCol.indexOf(filter) > -1 || thirdCol.indexOf(filter) > -1 || fourthCol.indexOf(filter) > -1) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
}

document.querySelector('#searchPrescribers').addEventListener('keyup', filterTable, false);


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