#include<iostream>
using namespace std;
int main(){
    cout<<"Cost Price : ";
    float c;
    cin>>c;
    cout<<"Selling Price : ";
    float s;
    cin>>s;
if(s>c){
    cout<<s-c;
    cout<<"\n\nYou got profit";}

if(c>s){
    cout<<c-s;
    cout<<"\n\nYou make loss";}

if(c==s){
    cout<<"\n\nYou have No profit and loss";}




    return 0;
}

