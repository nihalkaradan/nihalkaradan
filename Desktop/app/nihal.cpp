#include <iostream>
using namespace std;

int main() {
	int x;float y;
	cout<<"Input:\n";
	cin>>x>>y;
	if(x%5==0&&x<=y+.5)
	{
	    if(x>0&&x<=2000)
	    {
	        if(y>=0&&y<=2000)
	        {
	            y=y-x-.5;
	            
	        }
	    }
	}
	
	
	cout<<"Output:\n"<<y;
	
	return 0;
}
