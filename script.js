function generateEstimate() {
    

    let project = document.getElementById("project_name").value;
    let area = parseFloat(document.getElementById("area").value);

    let total_cost = area * 2200;
    let cement = area * 0.4;
    let steel = area * 4;
    let bricks = area * 8;

    document.getElementById("result").innerHTML = `
        <h2>Estimation Report</h2>
        <p><b>Project Name:</b> ${project}</p>
        <p><b>Area:</b> ${area} sq.ft</p>
        <p><b>Total Cost:</b> ₹${total_cost.toLocaleString()}</p>
        <p><b>Cement Bags:</b> ${cement}</p>
        <p><b>Steel Required:</b> ${steel} kg</p>
        <p><b>Bricks Required:</b> ${bricks}</p>
    `;
}