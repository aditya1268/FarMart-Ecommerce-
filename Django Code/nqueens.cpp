#include<iostream>
#include<bits/stdc++.h>
using namespace std;

void backtrack(vector<vector<int >>&v,int r,int n,set<int >pos,set<int>neg,set<int>col)
    {
        if(r==n)
        {
            for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (v[i][j] == 1) cout << 1;
                else cout << ". ";
            }
            cout << endl;
        }
        cout << endl;
        return;
            return ;
        }
        for (int c=0;c<n;c++)
        {
            if(col.find(c)!=col.end() || pos.find(c+r)!=pos.end() || neg.find(r-c )!=neg.end())
            {

                continue;
            }
            else 
            {
                col.insert(c);
                pos.insert(r+c);
                neg.insert(r-c);
                v[r][c]=1;

                backtrack(v,r+1,n,pos,neg,col);

                col.erase(c);
                pos.erase(r+c);
                neg.erase(r-c);
                v[r][c]=0;
            }
        }
    }

void nQueens(int n)
{
    set<int >col;
    set<int >pos;
    set<int >neg;
    vector<vector<int >>v;
    for(int i=0;i<n;i++)
    {
        vector<int >v1(n,0);
        v.push_back(v1);
    }
    
    backtrack(v,0,n,pos,neg,col);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout<<v[i][j]<<" ";
        }
        cout<<endl;
    }
}

int main()
{
    nQueens(5);
    return 0;
}


