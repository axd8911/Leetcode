```java
class RomanToInt {
    public int romanToInt(String s) {
        HashMap<Character,Integer> symbol = new HashMap<>();
        symbol.put('I',1);
        symbol.put('V',5);
        symbol.put('X',10);
        symbol.put('L',50);
        symbol.put('C',100);
        symbol.put('D',500);
        symbol.put('M',1000);
        
        int res = 0;
        
        for (int i=0;i<s.length()-1;i++){
            
            if (symbol.get(s.charAt(i)) >=symbol.get(s.charAt(i+1))){
                res += symbol.get(s.charAt(i));
            }
            else{
                res -= symbol.get(s.charAt(i));
            }
            
        }
        
        res += symbol.get(s.charAt(s.length()-1));
        return res;
    }
}
```