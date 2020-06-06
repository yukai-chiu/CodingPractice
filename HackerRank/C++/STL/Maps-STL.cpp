#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int q, type, mark;
    string name;
    cin >> q;
    map<string,int>m;
    for(int i=0;i<q;i++){
        cin >>type;
        if(type==1){
            cin >> name >> mark;
            if(m.find(name)==m.end()){
                m.insert(make_pair(name,mark));
            }
            else{
                m[name]+=mark;
            }
        }
        else if(type==2){
            cin >> name;
            m.erase(name);
        }
        else if(type==3){
            cin >> name;
            if(m.find(name)!=m.end()){
                cout << m[name] <<endl;
            }
            else{
                cout << 0<<endl;
            }
        }
        
    }

    return 0;
}



