// 8-clean_set.js
const cleanSet = (set, startString) => {
    return [...set]
      .filter(value => value.startsWith(startString))
      .map(value => value.slice(startString.length))
      .join('-');
  };
  
  export default cleanSet;
  