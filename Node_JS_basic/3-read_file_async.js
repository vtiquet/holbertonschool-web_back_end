const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const studentRecords = lines.slice(1);

      const totalStudents = studentRecords.length;
      let output = `Number of students: ${totalStudents}`;
      console.log(output);

      const fields = {};
      studentRecords.forEach((record) => {
        const student = record.split(',');
        const firstName = student[0];
        const field = student[3];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      const fieldNames = Object.keys(fields);
      fieldNames.forEach((field) => {
        const list = fields[field];
        const line = `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
        console.log(line);

        output += `\n${line}`;
      });

      resolve(output);
    });
  });
}

module.exports = countStudents;
