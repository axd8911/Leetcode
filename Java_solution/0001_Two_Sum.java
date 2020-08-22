import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> exist = new HashMap<>();
        
        for (int i=0;i<nums.length;i++){
            if (exist.containsKey(target-nums[i])){
                return new int[]{exist.get(target-nums[i]),i};
            }
            exist.put(nums[i],i);
        }
        return new int[]{};
        
    }
}