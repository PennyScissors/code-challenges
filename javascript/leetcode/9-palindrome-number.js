/*
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true

Example 2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. 
    From right to left, it becomes 121-. Therefore it is not a palindrome.
    
Example 3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
*/

var isPalindrome = function (x) {
    x_str = x.toString();

    for (let i = 0, k = x_str.length - 1; i < x_str.length; i++ , k--) {
        if (x_str[i] != x_str[k])
            return false;
    }

    return true;
};

console.log(isPalindrome(1221));
