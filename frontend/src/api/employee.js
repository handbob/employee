const BASE_URL = "http://localhost:8000/employees";

fetch(`${BASE_URL}/`, {
    method: "GET",
    mode: "cors",
    headers: {
        "Content-Type": "application/json"
    }
})
.then(response => response.json())
.then(data => {
    console.log(data);
})
.catch(error => {
    console.error("Error fetching data:", error);
});
