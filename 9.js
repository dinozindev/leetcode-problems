/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const xString = x.toString();
    let xArray = xString.split("").reverse();
    let xFinalString = "";
    for (let i = 0; i < xString.length; i++) {
        xFinalString+=xArray[i]; 
    }
    if (x.toString() == xFinalString) {
        return true  
    }
        return false
};