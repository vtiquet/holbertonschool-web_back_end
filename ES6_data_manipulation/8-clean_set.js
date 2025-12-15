export default function cleanSet(set, startString) {
  if (!startString || startString.length === 0 || !(set instanceof Set)) {
    return '';
  }

  const result = [];
  const startLength = startString.length;

  for (const value of set) {
    if (value && value.startsWith(startString)) {
      result.push(value.substring(startLength));
    }
  }

  return result.join('-');
}
