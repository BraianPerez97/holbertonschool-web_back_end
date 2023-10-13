// 1-get_list_student_ids.js
const getListStudentIds = (students) => (Array.isArray(students) ? students.map((student) => student.id) : []);

export default getListStudentIds;
