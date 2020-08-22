public class ParlindromeNumber {
    public boolean isPalindrome(int x) {
        if (x<0){return false;}
        
        int backup = x;
        int res = 0;
        while (x!=0){
            res *= 10;
            res += x%10;
            x/=10;
        }
        return backup==res;
    } 
}