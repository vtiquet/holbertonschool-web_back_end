const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      let output = `Number of students: ${students.length}\n`;
      const fields = {};

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      });

      const fieldKeys = Object.keys(fields);
      fieldKeys.forEach((field, index) => {
        output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
        if (index < fieldKeys.length - 1) output += '\n';
      });

      console.log(output);
      resolve(output);
    });
  });
}

module.exports = countStudents;
