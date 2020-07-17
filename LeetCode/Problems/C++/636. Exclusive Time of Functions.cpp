//Stack
//Time:O(n)
//Space: O(n), up to n/2
#include<iostream>
#include<stack>
#include<vector>
#include<sstream>

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        if(!n || !logs.size()) return {};
        
        vector<int> log_table;
        log_table.resize(n);
        stack<int> schedules; // id, timestamp
        int id, timestamp, prev;
        string status, temp1, temp2;
        
        for(string log: logs){
            stringstream ss(log);
            getline(ss, temp1, ':');
            getline(ss, status, ':');
            getline(ss, temp2, ':');
            id = stoi(temp1);
            timestamp = stoi(temp2);
            if(status == "start"){
                if(!schedules.empty())
                    log_table[schedules.top()] += timestamp - prev;
                schedules.push(id);
                prev = timestamp;   
            }
            else{
                //update when pop
                log_table[schedules.top()] += timestamp - prev + 1;
                schedules.pop();
                if(!schedules.empty())
                    prev = timestamp+1;
            }
        }
        return log_table;
    }
};

#include<iostream>
#include<stack>
#include<vector>
#include<sstream>

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        if(!n || !logs.size()) return {};
        
        vector<int> log_table;
        log_table.resize(n);
        stack<pair<int,int>> schedules; // id, timestamp
        int id, timestamp;
        string status, temp1, temp2;
        
        for(string log: logs){
            stringstream ss(log);
            getline(ss, temp1, ':');
            getline(ss, status, ':');
            getline(ss, temp2, ':');
            id = stoi(temp1);
            timestamp = stoi(temp2);
            if(status == "start"){
                if(!schedules.empty())
                    log_table[schedules.top().first] += timestamp - schedules.top().second;
                schedules.push({id, timestamp});
               
                
            }
            else{
                //update when pop
                log_table[schedules.top().first] += timestamp - schedules.top().second + 1;
                schedules.pop();
                if(!schedules.empty())
                    schedules.top().second = timestamp+1;
            }
        }
        
        return log_table;
    }
};