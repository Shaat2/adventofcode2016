#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>


bool isPossible(int a, int b, int c){
	return a+b>c && a+c>b && b+c>a;
}



int main(){
	std::ifstream stream;
	stream.open("input.txt");
	int count = 0;
	int possibleCount = 0;
	for (
		std::string line; std::getline(stream, line); 
		) {
        int a;
        int b;
        int c;
        sscanf(line.c_str(), "%d %d %d", &a,&b,&c);  
       	count++;
       	isPossible(a,b,c) ?  possibleCount++ : possibleCount;
    }
	stream.close();
	std::cout<<"All: " << count << " Possible: " << possibleCount;
}