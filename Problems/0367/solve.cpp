class Solution {
public:
    bool isPerfectSquare(int num) {
        int left = 0, right = num;
        while(right >= left){
            int half = left + (right - left) / 2;
            long square = (long)half * half;
            if(square < num){
                left = half + 1;
            }
            else if(square > num){
                right = half - 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};
