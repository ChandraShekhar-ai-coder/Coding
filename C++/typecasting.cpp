#include <iostream>
using namespace std;

int main()
{
    // int x;
    // cout<<"Enter Integer :";
    // cin>>x;
    // float y =(int) x;
    // cout<<(y/2);

    float y;
    cout << "Enter Decimal No. : ";

    cin >> y; // -0.1
    if (0 > y and y > -1)
    {
        y = 1 - y;
        cout << y;
    }

    int x = (int)y;

    if (x < -1)
    {
        x = x - 1;
        float z = (float)x;
        y = y - z;
        cout << y;
    }
}