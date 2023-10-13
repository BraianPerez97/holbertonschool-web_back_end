export default function cleanSet(_set, startString) {
    if (typeof _set !== 'object' || typeof startString !== 'string' || startString.length === 0) {
      return '';
    }
  
    const string = [];
  
    for (const item of _set) {
      if (item && item.startsWith(startString)) {
        string.push(item.slice(startString.length)).join('-');
      }
    }
    return string;
  }