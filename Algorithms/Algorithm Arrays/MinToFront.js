// Min to Front
// Given an array of comparable values, move the lowest element to array’s front, shifting backward any elements previously ahead of it.
//  Do not otherwise change the array’s order. Given [4,2,1,3,5], change it to [1,4,2,3,5] and return it. As always, do this without using built-in functions.

function MinToFront(arr) {
    if (arr.length === 0) {
        return arr; 
    }

    let min = 0; 
    for (let index = 1; index < arr.length; index++) {
        if (arr[index] < arr[min]) {
            min = index; 
        }
    }
    if (minIndex > 0) {
        const minValue = arr[min]; 
        for (let i = min; i > 0; i--) {
            arr[i] = arr[i - 1];
        }
        arr[0] = min;
    }

    return arr; 
}

// Examples
console.log(MinToFront([4, 2, 1, 3, 5])); // => [1, 4, 2, 3, 5]
console.log(MinToFront([10, 20, 5, 15])); // => [5, 10, 20, 15]