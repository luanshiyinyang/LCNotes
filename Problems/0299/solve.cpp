class Solution {
public:
    string getHint(string secret, string guess) {
        vector<int> secretNum(10), guessNum(10);
        int cows = 0, nulls = 0;
        for (int n = 0; n < secret.size(); n++){
            if(secret[n] == guess[n]){
                nulls++;
            } else{
                secretNum[secret[n] - '0']++;
                guessNum[guess[n] - '0']++;
            }
        }
        for (int i = 0; i < 10; i++){
            cows += min(secretNum[i], guessNum[i]);
        }
        string res = to_string(nulls) + 'A' + to_string(cows) + 'B';
        return res;
    }
};
