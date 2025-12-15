export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return 0;
  }

  return students.reduce((sum, student) => {
    return sum + student.id;
  }, 0);
}