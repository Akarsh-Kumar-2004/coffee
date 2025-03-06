# include <iostream>
# include <fstream>
# include <iomanip>
# include <string>
# include <cmath>
# include <cstring>
using namespace std;




int main(){
    cout<<endl;
    cout<<endl;
    cout<<endl;
    cout<<endl;
    int x;
    cin>>x;
    

    int dig = x;
    int rev = 0;
    if(x<0){
        return false;
    }

    while(x!=0){
        int rem = x%10;
        rev = rev*10 + rem;
        x = x/10;


    }
    if (rev == dig){
           cout<<"true";
    }
    else{
        cout<<"false";
    }




return 0;
}