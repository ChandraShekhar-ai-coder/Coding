#include<iostream>
#include <cmath> 
using namespace std;
int main(){
    cout<<"Enter a no. : ";
    int n;
    cin>>n;
    if( n%5 == 0){
        cout<<"No. is divisible by 5";
    }
    else{
        cout<<"No. is not divisible 5";
    }

    return 0;
}
// #include <iostream>
// #include <string>
// using namespace std;

// int main(){
//     cout << "Enter a no. : ";
//     string n; 
//     cin >> n;
    
//     // Get the last character of the string
//     char lastDigit = n.back(); 
    
//     if (lastDigit == '0' || lastDigit == '5'){
//         cout << "No. is divisible by 5";
//     }
//     else{
//         cout << "No. is not divisible 5";
//     }

//     return 0;
// }




// #include <iostream>
// using namespace std;

// int main(){
//     cout << "Enter a no. : ";
//     long long n; // Changed to long long
//     cin >> n;
    
//     if (n % 5 == 0){
//         cout << "No. is divisible by 5";
//     }
//     else{
//         cout << "No. is not divisible 5";
//     }

//     return 0;
// }