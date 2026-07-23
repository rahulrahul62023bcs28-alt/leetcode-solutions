class Solution {
    public int nthUglyNumber(int n) {
        int[] ugly = new int[n];
        ugly[0] = 1;
        
        int trackTwo = 0;
        int trackThree = 0;
        int trackFive = 0;
        
        for (int i = 1; i < n; i++) {
            int optionA = ugly[trackTwo] * 2;
            int optionB = ugly[trackThree] * 3;
            int optionC = ugly[trackFive] * 5;
            
            int lowestVal = optionA;
            if (optionB < lowestVal) {
                lowestVal = optionB;
            }
            if (optionC < lowestVal) {
                lowestVal = optionC;
            }
            
            ugly[i] = lowestVal;
            
            if (lowestVal == optionA) {
                trackTwo = trackTwo + 1;
            }
            if (lowestVal == optionB) {
                trackThree = trackThree + 1;
            }
            if (lowestVal == optionC) {
                trackFive = trackFive + 1;
            }
        }
        
        return ugly[n - 1];
    }
}
