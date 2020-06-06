#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    vector<int> v(n);
    for(int i=0;i<n;i++){
        cin >> v[i];
    }
    int i,j;
    cin >> i;
    v.erase(v.begin()+i-1);
    cin >>i >>j;
    v.erase(v.begin()+i-1,v.begin()+j-1);
    cout << v.size() << endl;
    for(int i=0;i<v.size();i++){
        cout << v[i] <<" ";
    }
    return 0;
}
