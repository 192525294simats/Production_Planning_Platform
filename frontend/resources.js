const machineStatus = {
    "Machine 1": "Available",
    "Machine 2": "In Use",
    "Machine 3": "Maintenance"
};

function assignMachine() {

    const machine = document.getElementById("machine").value;

    const result = document.getElementById("machineResult");

    if (machineStatus[machine] === "Available") {

        result.innerHTML =
            "✓ Machine assignment successful.";

    } else {

        result.innerHTML =
            "⚠ Assignment rejected: " +
            machine +
            " is " +
            machineStatus[machine] +
            ".";
    }
}