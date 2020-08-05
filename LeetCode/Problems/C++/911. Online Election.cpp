//Precompute + binary search
//Time: O(n + qlogn)
//Space: O(n)
class TopVotedCandidate {
public:
    TopVotedCandidate(vector<int>& persons, vector<int>& times) {
        unordered_map<int, int> counter{0};
        int max_vote = 0, lead = 0;
        for(int i=0;i<persons.size();i++){
            counter[persons[i]]+=1;
            if(counter[persons[i]] >= max_vote){
                lead = persons[i];
                max_vote = counter[persons[i]];
            }
            leader[times[i]] = lead;
        }   
        time_stamp = &times;
    }
    
    int q(int t) {
        int lo = 0;
        int hi = (*time_stamp).size();
        
        if(leader.find(t)!=leader.end()) 
            return leader[t];
        while(lo <hi){
            int mid = lo + (hi-lo)/2;
            if((*time_stamp)[mid] >t) 
                hi = mid;
            else 
                lo = mid+1;
        }
        return leader[(*time_stamp)[hi-1]];
    }
private:
    vector<int>* time_stamp;
    unordered_map<int, int> leader;
};