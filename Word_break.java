class Solution {
    public boolean wordBreak(String s, List<String> wordDict) 
    {
        int stringLength =s.length();
        boolean[] dp=new boolean[stringLength+1];
        dp[0]=true;
        for(int i=0;i<stringLength;i++)
        {
            if(!dp[i])
            {
                continue;
            }
            for (int w=0;w<wordDict.size();w++)
            {
                String word=wordDict.get(w);
                int wordLength=word.length();
                if(i+wordLength>stringLength)
                {
                    continue;
                }
                boolean isMatch=true;
                for(int k=0;k<wordLength;k++)
                {
                    if(s.charAt(i+k)!=word.charAt(k))
                    {
                        isMatch=false;
                        break;
                    }
                }
                if(isMatch)
                {
                    dp[i+wordLength]=true;
                }
            }
        }
        return dp[stringLength];

    }
}
