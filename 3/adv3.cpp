#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <string>

bool isPossible(int a, int b, int c){
	return a+b>c && a+c>b && b+c>a;
}

int main(){
	std::ifstream stream;
	stream.open("input.txt");
	int count = 0;
	int possibleCount = 0;
	for (
		std::vector<std::string> lines{3}; 
		std::getline(stream, lines[0]) && std::getline(stream, lines[1]) && std::getline(stream, lines[2]);
		) 
	{
		std::vector<std::vector<int>> sides{};

		for(int i=0; i<3;++i){
			std::vector<int> side{0,0,0};
			int a,b,c;
	        sscanf(lines[i].c_str(), "%d %d %d", &a,&b,&c);  
	        side[0] = a;
			side[1] = b;
			side[2] = c;
	       	count++;
	       	sides.push_back(side);
		}
		for(int i=0; i<3;++i){
			isPossible(sides[0][i], sides[1][i], sides[2][i]) ?  possibleCount++ : possibleCount;
		}

    }
	stream.close();
	std::cout<<"All: " << count << " Possible: " << possibleCount;
}