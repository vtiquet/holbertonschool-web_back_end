const fs = require('fs');

async function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.trim().split('\n').filter((line) => line !== '');
      const students = lines.slice(1);
      let response = `Number of students: ${students.length}\n`;
      const fields = {};

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      });

      const fieldEntries = Object.entries(fields);
      fieldEntries.forEach(([field, names], index) => {
        response += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        if (index < fieldEntries.length - 1) response += '\n';
      });

      console.log(response);
      resolve(response);
    });
  });
}

module.exports = countStudents;
