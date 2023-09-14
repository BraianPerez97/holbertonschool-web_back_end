export default function createIteratorObject(report) {
  const allEmployees = report.allEmployees;
  const departments = Object.keys(allEmployees);
  let departmentIndex = 0;
  let employeeIndex = 0;

  return {
    next() {
      if (departmentIndex < departments.length) {
        const department = departments[departmentIndex];
        const employeesInDepartment = allEmployees[department];

        if (employeeIndex < employeesInDepartment.length) {
          const employee = employeesInDepartment[employeeIndex];
          employeeIndex++;
          return { value: employee, done: false };
        } else {
          departmentIndex++;
          employeeIndex = 0;
          return this.next();
        }
      } else {
        return { done: true };
      }
    },
  };
}
