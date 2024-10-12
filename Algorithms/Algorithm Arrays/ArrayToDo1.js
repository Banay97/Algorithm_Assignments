// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!

function myFrontPush(array , element){
    for( var i = array.length ; i > 0 ; i--){
        array[i]= array[i-1]
    }
    array[0] = element;
    return array.length;

}

// Examples:
let fruits = ['banana', 'orange'];
let newLength = myFrontPush(fruits, 'apple');
console.log(fruits); // ['apple', 'banana', 'orange']
console.log(newLength); //3

let arrayOfNumbers = [5,7,2,3]
let newLengthForArrayOfNumbers = myFrontPush(arrayOfNumbers, 8)
console.log(arrayOfNumbers) // pushFront([5,7,2,3], 8) => [8,5,7,2,3]
console.log(newLengthForArrayOfNumbers)//5


// Pop Front
// Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!

function myFrontPop(array, element){
    if(array.length === 0){
        return  undefined; 
    }else{
        let firstElement = array[0]
        for (let i = 0; i < array.length - 1; i++) {
            array[i] = array[i + 1];
        }
    array.length = array.length - 1; 
    return firstElement;
    }
}
// Examples:
let fruits1 = ['apple', 'banana'];
let removedFruit = myFrontPop(fruits1);
console.log(fruits1); // ['banana']
console.log(removedFruit); // 'apple'

let arrayOfNumbers1 = [5, 7, 2, 3];
let newLengthForArrayOfNumbers1 = myFrontPop(arrayOfNumbers1);
console.log(arrayOfNumbers1); // [7, 2, 3]
console.log(newLengthForArrayOfNumbers1); // 5

// popFront([0,5,10,15]) => 0 returned, with [5,10,15] printed in the function
// popFront([4,5,7,9]) => 4 returned, with [5,7,9] printed in the function

// Insert At
// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!

// Examples:

// insertAt([100,200,5], 2, 311) => [100,200,311,5]
// insertAt([9,33,7], 1, 42) => [9,42,33,7]
function insert_at(arr, value){
    const new_array = []
    for(var index = 0 ; index <arr.length ; index++){
        if(index === value){
            new_array.push(value)

        }
        new_array.push(arr[index])

    }
    if(index === arr.length){
        new_array.push(value)
    }
return new_array

}


console.log(insert_at([100, 200, 5], 2, 311)); // => [100, 200, 311, 5]
console.log(insert_at([9, 33, 7], 1, 42)); // => [9, 42, 33, 7]

// BONUS: Remove At
// Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it. Think of popFront(arr) as equivalent to removeAt(arr,0).

// Examples:

// removeAt([1000,3,204,77], 1) => 3 returned, with [1000,204,77] printed in the function
// removeAt([8,20,55,44,98], 3) => 44 returned, with [8,20,55,98] printed in the function

function remove_at(arr, index) {
    if (index < 0 || index >= arr.length) {
        return null; 
    }

    const removed_value = arr[index];
    const new_array = [];

    for (var i = 0; i < arr.length; i++) {
        
        if (i !== index) {
            new_array.push(arr[i]);
        }
    }
    console.log(new_array);

    return removed_value;
}

// Examples:
console.log(remove_at([1000, 3, 204, 77], 1)); // => 3, [1000, 204, 77] printed
console.log(remove_at([8, 20, 55, 44, 98], 3)); // => 44, [8, 20, 55, 98] printed

// BONUS: Swap Pairs
// Swap positions of successive pairs of values of given array. If length is odd, do not change the final element.

// Examples:

// swap([1,2,3,4]) => [2,1,4,3]
// swap​(["Brendan",true,42]) => [true,"Brendan",42]

// BONUS: Remove Duplicates
// Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. If you already made the Remove At function, you are welcome to use that! If you solved this using nested loops, for an extra challenge, try to do it without any nested loops!

// Examples:

// removeDupes([-2,-2,3.14,5,5,10]) => [-2,3.14,5,10]
// removeDupes([9,19,19,19,19,19,29]) => [9,19,29]