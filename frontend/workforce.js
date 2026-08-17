const workerStatus = {
    "Worker 1": "Available",
    "Worker 2": "Assigned",
    "Worker 3": "Available",
    "Worker 4": "On Leave"
};

function assignWorker() {

    const worker = document.getElementById("worker").value;

    const result = document.getElementById("workerResult");

    if (workerStatus[worker] === "Available") {

        result.innerHTML =
            "✓ Worker assignment successful.";

    } else {

        result.innerHTML =
            "⚠ Assignment rejected: " +
            worker +
            " is " +
            workerStatus[worker] +
            ".";
    }
}