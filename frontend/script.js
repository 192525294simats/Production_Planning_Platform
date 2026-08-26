console.log("Production Planning Platform loaded successfully.");

async function loadDashboardData() {
    try {
        // Get production orders
        const ordersResponse = await fetch("http://localhost:5001/api/orders");
        const orders = await ordersResponse.json();

        // Get inventory
        const inventoryResponse = await fetch("http://localhost:5001/api/inventory");
        const inventory = await inventoryResponse.json();

        // Get resources
        const resourcesResponse = await fetch("http://localhost:5001/api/resources");
        const resources = await resourcesResponse.json();

        // Display counts
        displayCount("production-orders", orders.length);
        displayCount("inventory-items", inventory.length);
        displayCount("manufacturing-resources", resources.length);

        console.log("Orders:", orders);
        console.log("Inventory:", inventory);
        console.log("Resources:", resources);

    } catch (error) {
        console.error("Error loading dashboard data:", error);
    }
}


function displayCount(elementId, count) {
    const element = document.getElementById(elementId);

    if (element) {
        element.textContent = count;
    } else {
        console.warn("Element not found:", elementId);
    }
}


document.addEventListener("DOMContentLoaded", function () {
    loadDashboardData();
});
