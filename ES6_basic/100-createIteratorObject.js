export default function createIteratorObject(Report) {
  let results = [];
  for (const value of Object.values(Report.allEmployees)) {
    results = [...results, ...value];
  }
  return results;
}
