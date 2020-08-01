class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        if(!tasks.size()) return 0;
        
        int count[26]{};
        int max_idle;
        int ptr = 24;
        for(int i=0;i<tasks.size();i++) {
            count[tasks[i]-'A']+=1;
        }
        sort(count, count+26);
        
        max_idle = (count[25]-1) * n;
        
        while(ptr>=0 && max_idle >= 0)
            max_idle-=min(count[25]-1,count[ptr--]);
        
        max_idle = max(0, max_idle);
        
        return max_idle + tasks.size();    
    }
};