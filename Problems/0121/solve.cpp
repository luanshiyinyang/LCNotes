class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX, res = 0;
        for(int price : prices){
            res = max(res, price - minPrice);
            minPrice = min(minPrice, price);
        }
        return res;
    }
};
