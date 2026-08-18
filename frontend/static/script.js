let departmentChart;
let passFailChart;
let marksChart;
let attendanceChart;
let semesterChart;


function removeOldCharts() {

    if (departmentChart) {
        departmentChart.destroy();
    }

    if (passFailChart) {
        passFailChart.destroy();
    }

    if (marksChart) {
        marksChart.destroy();
    }

    if (attendanceChart) {
        attendanceChart.destroy();
    }

    if (semesterChart) {
        semesterChart.destroy();
    }
}


async function loadDashboard() {

    try {

        const response = await fetch("/api/dashboard");
        const data = await response.json();

        if (data.error) {
            alert(data.error);
            return;
        }


        // Update dashboard numbers

        document.getElementById("totalStudents").textContent =
            data.total_students;

        document.getElementById("averageMarks").textContent =
            data.average_marks + "%";

        document.getElementById("averageAttendance").textContent =
            data.average_attendance + "%";

        document.getElementById("topStudent").textContent =
            data.top_student_name;

        document.getElementById("topMarks").textContent =
            data.top_student_marks + "% marks";


        removeOldCharts();


        // Department chart

        departmentChart = new Chart(
            document.getElementById("departmentChart"),
            {
                type: "bar",

                data: {
                    labels: data.department_names,

                    datasets: [{
                        label: "Students",
                        data: data.department_counts,

                        backgroundColor: [
                            "#6366f1",
                            "#8b5cf6",
                            "#ec4899",
                            "#06b6d4",
                            "#14b8a6",
                            "#f59e0b"
                        ],

                        borderRadius: 7
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    plugins: {
                        legend: {
                            display: false
                        }
                    },

                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                precision: 0
                            }
                        }
                    }
                }
            }
        );


        // Pass fail chart

        passFailChart = new Chart(
            document.getElementById("passFailChart"),
            {
                type: "doughnut",

                data: {
                    labels: ["Passed", "Failed"],

                    datasets: [{
                        data: [
                            data.passed_students,
                            data.failed_students
                        ],

                        backgroundColor: [
                            "#10b981",
                            "#ef4444"
                        ],

                        borderWidth: 0
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    cutout: "65%",

                    plugins: {
                        legend: {
                            position: "bottom"
                        }
                    }
                }
            }
        );


        // Department marks

        marksChart = new Chart(
            document.getElementById("marksChart"),
            {
                type: "bar",

                data: {
                    labels: data.department_marks_names,

                    datasets: [{
                        label: "Average Marks",
                        data: data.department_average_marks,

                        backgroundColor: "#8b5cf6",

                        borderRadius: 7
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 100
                        }
                    },

                    plugins: {
                        legend: {
                            display: false
                        }
                    }
                }
            }
        );


        // Attendance chart

        attendanceChart = new Chart(
            document.getElementById("attendanceChart"),
            {
                type: "line",

                data: {
                    labels: data.department_attendance_names,

                    datasets: [{
                        label: "Attendance",
                        data: data.department_average_attendance,

                        borderColor: "#06b6d4",
                        backgroundColor: "rgba(6,182,212,0.12)",

                        fill: true,
                        tension: 0.3
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 100
                        }
                    }
                }
            }
        );


        // Semester chart

        semesterChart = new Chart(
            document.getElementById("semesterChart"),
            {
                type: "line",

                data: {
                    labels: data.semester_names,

                    datasets: [{
                        label: "Students",
                        data: data.semester_counts,

                        borderColor: "#ec4899",
                        backgroundColor: "rgba(236,72,153,0.12)",

                        fill: true,
                        tension: 0.3
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                precision: 0
                            }
                        }
                    }
                }
            }
        );


        // Department table

        const table =
            document.getElementById("departmentTableBody");

        table.innerHTML = "";


        if (!data.department_performance.length) {

            table.innerHTML = `
                <tr>
                    <td colspan="6" class="empty">
                        No department data available.
                    </td>
                </tr>
            `;

            return;
        }


        data.department_performance.forEach(function(department) {

            const row = document.createElement("tr");

            row.innerHTML = `
                <td>
                    <strong>${department.department}</strong>
                </td>

                <td>
                    ${department.total_students}
                </td>

                <td>
                    <span class="marks-value">
                        ${department.average_marks || 0}%
                    </span>
                </td>

                <td>
                    ${department.average_attendance || 0}%
                </td>

                <td>
                    <span class="pass">
                        ${department.passed || 0}
                    </span>
                </td>

                <td>
                    <span class="fail">
                        ${department.failed || 0}
                    </span>
                </td>
            `;

            table.appendChild(row);
        });

    }

    catch (error) {

        console.log("Dashboard error:", error);

    }
}


document.addEventListener("DOMContentLoaded", function() {

    if (document.getElementById("departmentChart")) {
        loadDashboard();
    }

});