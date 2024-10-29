/**
 * @param {string} s
 * @return {number}
 */
var minLength = function(s) {
    d = s.length
    for (let i = 0; i < d; i++) {
        if (s.includes("AB")) {
            s = s.replace("AB", "")
        } else if (s.includes("CD")) {
            s = s.replace("CD", "") 
        }
        
    }
    return s.length;
};