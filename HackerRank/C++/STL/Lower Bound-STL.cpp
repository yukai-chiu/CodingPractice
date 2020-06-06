#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, q, query, idx;
    cin >> n;
    vector<int> v(n);
    for(int i=0;i<n;i++){
        cin >> v[i];
    }   
    cin >> q;

    vector<int>::iterator low;
    for(int i =0;i<q;i++){
        cin >> query;
        low = lower_bound(v.begin(),v.end(),query);
        idx = low - v.begin();
        if(v[idx] == query){
            cout << "Yes " << idx+1 << endl;
        }
        else{
            cout <<"No " << idx+1 << endl;
        }

    }
    
    return 0;
}
