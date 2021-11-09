// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int start = 1, end = n, mid;
        if(isBadVersion(1)){
            return 1;
        }
        while(start <= end){
            mid = start + (end - start) / 2;
            if(isBadVersion(mid) && !isBadVersion(mid - 1)){
                return mid;
            } else if(!isBadVersion(mid)){
                start = mid + 1;
            } else{
                end = mid - 1;
            }
        }
        return 0;
    }
};
