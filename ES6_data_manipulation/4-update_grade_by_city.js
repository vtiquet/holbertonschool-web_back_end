export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }

  const cityStudents = students.filter((student) => student.location === city);

  return cityStudents.map((student) => {
    const gradeObject = newGrades.find(
      (grade) => grade.studentId === student.id
    );

    return {
      ...student,
      grade: gradeObject ? gradeObject.grade : 'N/A',
    };
  });
}