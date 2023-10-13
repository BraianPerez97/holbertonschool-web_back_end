// 5-typed_arrays.js
const createInt8TypedArray = (length, position, value) => {
  const buffer = new ArrayBuffer(length);
  const dataView = new DataView(buffer);

  if (position >= 0 && position < length) {
    dataView.setInt8(position, value);
    return dataView;
  }
  throw new Error('Position outside range');
};

export default createInt8TypedArray;
