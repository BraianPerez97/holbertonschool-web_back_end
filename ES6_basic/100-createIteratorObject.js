export default function createIteratorObject(report) {
  const departments = Object.keys(report.allEmployees);
  let departmentIndex = 0;
  let employeeIndex = 0;

  const iterator = {
    next() {
      if (departmentIndex < departments.length) {
        const department = departments[departmentIndex];
        const employeesInDepartment = report.allEmployees[department];

        if (employeeIndex < employeesInDepartment.length) {
          const employee = employeesInDepartment[employeeIndex];
          employeeIndex++;
          return { value: employee, done: false };
        }
        departmentIndex++;
        employeeIndex = 0;
        return this.next();
      }
      return { done: true };
    },
    [Symbol.iterator]() {
      return this;
    },
  };

  return iterator;
}
