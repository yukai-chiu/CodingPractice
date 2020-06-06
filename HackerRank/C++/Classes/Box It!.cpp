#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box
class Box{
    private:
        long long l;
        long long b;
        long long h;

    public:
        Box(){
            l = 0;
            b = 0;
            h = 0;
        }
        Box(int _l, int _b, int _h){
            l = _l;
            b = _b;
            h = _h;
        }

        int getLength(){
            return l;
        }

        int getBreadth(){
            return b;
        }

        int getHeight(){
            return h;
        }

        long long CalculateVolume(){
            return l*b*h;
        }

        bool operator <(Box& B){
            if (l < B.l){
                return true;
            }
            else if(b < B.b && l == B.l){
                return true;
            }
            else if(h < B.h && b == B.b && l == B.l){
                return true;
            }
            return false;

        }
        friend ostream& operator <<(ostream& out, Box& B);

};

ostream& operator <<(ostream& out, Box& B){
            
    out << B.l << " " << B.b << " " << B.h;
    return out;
}

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

