// Array to store employees
const employees = [
  { id: 1, name: "Yashas S", phone: 60000 },
  { id: 2, name: "Zaid", phone: 50000 },
];

const employeeTableBody = document.getElementById("table-data");
const empNameInput = document.getElementById("name");
const empPhoneInput = document.getElementById("phone");

// Function to render employees in the table
function renderEmployeeTable() {
  employeeTableBody.innerHTML = "";
  employees.forEach((employee, index) => {
    const row = document.createElement("tr");
    row.innerHTML = `
            <td>${index + 1}</td>
            <td>${employee.name}</td>
            <td>${employee.phone}</td>
            <td>
              <button onclick="editEmployee(${employee.id})">Edit</button>
              <button onclick="deleteEmployee(${employee.id})">Delete</button>
            </td>
          `;
    employeeTableBody.appendChild(row);
  });
}

// Handle form submission to add new employees
document
  .getElementById("employee-form")
  .addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent page reload

    const name = empNameInput.value.trim();
    const phone = empPhoneInput.value.trim();

    if (name === "" || phone === "") {
      alert("Please fill in all fields.");
      return;
    }

    // Generate a unique ID
    const newEmployee = {
      id: employees.length + 1,
      name: name,
      phone: phone,
    };

    employees.push(newEmployee); // Add new employee to the array
    renderEmployeeTable(); // Re-render the table
    empNameInput.value = ""; // Clear input fields
    empPhoneInput.value = "";
  });

// Initial render of the table
renderEmployeeTable();
