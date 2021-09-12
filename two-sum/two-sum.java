class Solution {
    public int[] twoSum(int[] nums, int target) 
    {
        //target = 9
        //nums = [2,7,11,15]
        //map = [(0,2),(1,7),(2,11),(3,15)]
        
        HashMap map = new HashMap<Integer,Integer>();
        for (int i=0; i<nums.length; i++)
        {
            int remaining = target - nums[i];
            if (map.containsKey(remaining))
            {
                return new int[]{i,(int)map.get(remaining)};
            }
            else
            {
                map.put(nums[i],i);
            }
        }
        return null;
    }
}