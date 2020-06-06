#include <iostream>

using namespace std;
/*
 * Create classes Rectangle and RectangleArea
 */
class Rectangle{
    protected:
        int width;
        int height;
    public:
        void display(){
            cout<<this->width<<" "<<this->height<<endl;
        }

};

class RectangleArea: public Rectangle{
    public:
        void read_input(){
            cin >> this->width;
            cin >> this->height;
        }
        void display(){
            cout<<this->width*this->height<<endl;
        }

};
