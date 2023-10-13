// 3-get_ids_sum.js
const getStudentIdsSum = (students) => students.reduce((sum, student) => sum + student.id, 0);

export default getStudentIdsSum;
