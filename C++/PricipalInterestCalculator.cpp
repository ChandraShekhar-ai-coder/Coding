#include<iostream> 
#include <cmath> 
using namespace std; 

int main() {
    float p, i, t;
    
    // Input: Principal, Interest rate (or amount), and Time
    cout<<"Principal : ";
    cin >> p ;
    cout<<"Interest(In Percentage per Year) : ";
    cin >> i; 
    cout<< "Time(In Years) : ";
    cin >> t;


    // Output: Added spaces and newlines (\n) for readability
    cout << "Principal: " << p << "\nInterest: " << i << "\nTime: " << t << "\n";

    
    float simple_interest = (p*i*t)/100;
    cout << "\n--- Simple Interest Calculation ---" << endl;
    cout << "Interest Earned: " << simple_interest << endl;

    float total_simple_balance = p + simple_interest;
    cout<<"\n--- Simple Balance Calculation ---"<<endl;
    cout <<"Total Simple Balance : "<<total_simple_balance <<endl;
    float r = i/100;
    float total_compound_balance = p * std::pow((1 + r), t);
    float compound_interest = total_compound_balance - p;
    cout << "Compound Balance: " << total_compound_balance << endl;
    cout << "Compound Interest : " << compound_interest << endl;
    
    return 0;
}
