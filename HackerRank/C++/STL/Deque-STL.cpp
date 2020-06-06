#include <iostream>
#include <deque> 
using namespace std;

void printKMax(int arr[], int n, int k){
	//Write your code here.
    deque<int>d;
    

    for(int i=0;i<n;i++){
        //if the left element in deque in out of bound
        if(i>=k && i-k == d[0]){
            d.pop_front();
        }

        //maintain the decrease of the queue
        while(d.size()>0 && arr[i] > arr[d.back()]){
            d.pop_back();
        }
        d.push_back(i);

        if(i >=k-1){
            cout << arr[d.front()] << " ";
        }
    } 
    
    cout << endl;



}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}
