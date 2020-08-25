```java
class Solution {
    public String thousandSeparator(int n) {
        
        StringBuilder res = new StringBuilder();
        String nStr = Integer.toString(n);
        
        for (int i=0;i<nStr.length();++i){
            if (i!=0 && (nStr.length()-i) % 3 == 0){
                res.append(".");
            }
            res.append(nStr.charAt(i));
        }

        return res.toString();
        
    }
}
```