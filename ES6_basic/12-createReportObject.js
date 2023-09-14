export default function iterateThroughObject(reportWithIterator) {
  const employees = [...reportWithIterator.allEmployees];
  return employees.join(' | ');
}
