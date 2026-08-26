const inventory = {
    Steel: 500,
    Plastic: 300,
    Aluminium: 200
};

function checkInventory() {

    const material = document.getElementById("material").value;

    const required = Number(
        document.getElementById("required").value
    );

    const available = inventory[material];

    const result = document.getElementById("result");

    if (required <= 0 || isNaN(required)) {

        result.innerHTML =
            "Please enter a valid quantity.";

    } else if (required <= available) {

        result.innerHTML =
            "✓ Material Available";

    } else {

        result.innerHTML =
            "⚠ Alert: Insufficient " +
            material +
            " for Production Order.";

    }
}
