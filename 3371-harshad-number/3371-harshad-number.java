class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int sumOfDigits = 0;
        int temp = x;
        
        while (temp > 0) {
            sumOfDigits += temp % 10;
            temp /= 10;
        }
        // Check if x is a Harshad number
        if (x % sumOfDigits == 0) {
            return sumOfDigits; // Return the sum of digits if x is a Harshad number
        } else {
            return -1; // Return -1 if x is not a Harshad number
        }
    }
}