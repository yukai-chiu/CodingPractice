class Solution {
public:
    string addStrings(string num1, string num2) {
        if(!num1.size()) return num2;
        if(!num2.size()) return num1;
        
        int n1 = num1.size()-1, n2 = num2.size()-1, sum;
        int carry = 0;
        string result;
        int r = max(n1,n2);
        result.resize(r+1);
        

        while(n1 >=0 && n2 >=0){
            sum = num1[n1] - '0' + num2[n2] - '0'+ carry;
            carry = sum / 10;
            result[r--] = sum % 10 + '0';
            n1--;
            n2--;
        }
        while(n1 >= 0){
            sum = num1[n1] - '0' + carry;
            carry = sum / 10;
            result[r--] = sum %10 + '0';
            n1--;
        }
        while(n2 >=0){
            sum = num2[n2] - '0' + carry;
            carry = sum / 10;
            result[r--] = sum %10 + '0';
            n2--;
        }
        if(carry != 0){
            result = "1" + result;
        }
        return result;
    }
};