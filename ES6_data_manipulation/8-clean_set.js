export default function cleanSet(_set, startString) {
    if (!(typeof _set === 'object' && _set instanceof Set) || typeof startString !== 'string' || startString.length === 0) {
      return '';
    }
  
    const string = [];
  
    // Convert the Set to an array
    const setArray = Array.from(_set);
  
    for (const item of setArray) {
      if (item && item.startsWith(startString)) {
        string.push(item.slice(startString.length));
      }
    }
  
    // Join outside the loop to concatenate all strings
    return string.join('-');
  }
  