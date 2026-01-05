const fs = require('fs');

/**
 * Counts students from a CSV file asynchronously.
 * @param {string} path - The path to the CSV file.
 * @returns {Promise<void>}
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      if (students.length === 0) {
        console.log('Number of students: 0');
        resolve();
        return;
      }

      console.log(`Number of students: ${students.length}`);

      const fields = {};
      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      for (const [field, names] of Object.entries(fields)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
