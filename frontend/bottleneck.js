function detectBottleneck() {

    const requiredMaterial =
        Number(document.getElementById("requiredMaterial").value);

    const availableMaterial =
        Number(document.getElementById("availableMaterial").value);

    const machineStatus =
        document.getElementById("machineStatus").value;

    const requiredWorkers =
        Number(document.getElementById("requiredWorkers").value);

    const availableWorkers =
        Number(document.getElementById("availableWorkers").value);

    const result =
        document.getElementById("bottleneckResult");

    let bottlenecks = [];

    if (requiredMaterial > availableMaterial) {
        bottlenecks.push("⚠ Material Bottleneck");
    }

    if (machineStatus === "Unavailable") {
        bottlenecks.push("⚠ Machine Bottleneck");
    }

    if (requiredWorkers > availableWorkers) {
        bottlenecks.push("⚠ Workforce Bottleneck");
    }

    if (bottlenecks.length === 0) {

        result.innerHTML =
            "✓ No bottlenecks detected.";

    } else {

        result.innerHTML =
            bottlenecks.join("<br>");
    }
}