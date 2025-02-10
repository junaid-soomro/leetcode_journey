function solve(n, array, k) {
  const minArr = [...array];
  const maxArr = [...array];

  for (let i = 0; i < k; i++) {
    const max = findMax(maxArr);
    maxArr.splice(maxArr.indexOf(max), 1);

    const min = findMin(minArr);
    minArr.splice(minArr.indexOf(min), 1);
  }

  const maxValue = maxArr.reduce((arr, item) => (arr += item), 0);
  const minValue = minArr.reduce((arr, item) => (arr += item), 0);

  console.log("max value is: ", maxValue);
  console.log("min value is: ", minValue);

  return [maxValue, minValue];
}

function findMax(arr) {
  let max = arr[0];

  for (let i = 0; i < arr.length; i++) {
    if (max < arr[i]) {
      max = arr[i];
    }
  }

  return max;
}

function findMin(arr) {
  let max = arr[0];

  for (let i = 0; i < arr.length; i++) {
    if (max > arr[i]) {
      max = arr[i];
    }
  }

  return max;
}

solve(5, [1.5, 2.5, 3.5, 4.5], 1);
