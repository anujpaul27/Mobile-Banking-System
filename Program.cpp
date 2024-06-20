#include <bits/stdc++.h>
using namespace std;

int main ()
{
    //create vector with n size 
    int n;
    cin>>n;
    vector <int> v;
    
    //Input This vector with indexing for loops 
    for (int i=0; i<n; i++)
    {
        cin>>v[i];
    }

    // output input vector 
    for (int i=0; i<n; i++)
    {
        cout<<v[i]<<" ";
    }

    return 0;
}