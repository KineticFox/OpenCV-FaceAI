#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <ctime>

using namespace std;

int randn(){

	srand(time(NULL));
	int v = rand() % 100 +1;
	return v;
}


int main(int argc, char const *argv[])
{
	
	cout << randn();
}