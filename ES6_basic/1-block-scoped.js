export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    task = true; // No need to redeclare using let here, just assign the new value
    task2 = false; // No need to redeclare using let here, just assign the new value
  }

  return [task, task2];
}
