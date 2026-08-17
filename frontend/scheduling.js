function createSchedule() {

    const product = document.getElementById("product").value;
    const quantity = document.getElementById("quantity").value;
    const startDate = document.getElementById("startDate").value;
    const endDate = document.getElementById("endDate").value;
    const machine = document.getElementById("machine").value;
    const workers = document.getElementById("workers").value;
    const priority = document.getElementById("priority").value;

    const result = document.getElementById("scheduleResult");

    if (
        quantity === "" ||
        startDate === "" ||
        endDate === "" ||
        workers === ""
    ) {
        result.innerHTML = "Please fill all required fields.";
        return;
    }

    result.innerHTML =
        "✓ Production schedule created successfully for " +
        product +
        " (" +
        quantity +
        " units).";
}