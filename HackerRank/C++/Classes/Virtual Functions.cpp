#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
//he class Person should have data members name and age
class Person{
    protected:
        string name;
        int age;
        
    public:
        static int count;
        virtual void getdata(){};
        virtual void putdata(){};
};
class Professor: public Person{
    private:
        int publications;
        int cur_id;
        
    public:
        static int id;
        Professor(){
            this->cur_id = ++id; 
        };
        void getdata(){
            cin >> this->name >> this->age >> this->publications;
        }
        void putdata(){
            cout << this->name << " " << this->age << " " << this->publications << " " <<  this->cur_id << endl;
        }
};
int Professor::id = 0;
class Student: public Person{
    private:
        int marks[6];
        int cur_id;

        
    public:
        static int id;
        Student(){
            this->cur_id = ++id;
        };
        void getdata(){
            cin >> this->name >> this->age;
            for(int i=0;i<6;i++){
                cin >> this->marks[i];
            }
        }
        void putdata(){
            cout << this->name << " " << this->age << " ";
            int sum = 0;
            for(int i=0;i<6;i++){
                sum+= this->marks[i];
            }
            cout << sum << " " << this->cur_id << endl;
        }

};
int Student::id = 0;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
