/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int lo = 1;
        int hi = n;
        int mid, guessed;
        while(lo<=hi){
            mid = lo + (hi-lo)/2;
            guessed = guess(mid);
            if(guessed == 0)
                break;
            else if(guessed == -1)
                hi = mid-1;
            else
                lo = mid+1;
        }
        return mid;
    }
};