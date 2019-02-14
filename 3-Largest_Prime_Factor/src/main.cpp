/*

Problem Statement:

The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?

src: https://projecteuler.net/problem=3

*/


#include <stdio.h>
#include <iostream>

bool isPrime(int num);

int main(int argc, char** argv)
{
	try
	{
		// default number is 600851475143 but allow user can override
		auto num = (argc > 1) ? atoi(argv[1]) : 600851475143;
		
		// Solution 1 ( O(n^2) )
		for (auto i = 2U; i <= num; ++i)
		{
			if ( num % i == 0 && isPrime (num / i))
			{
				std::cout << "The largest prime factor of " << num << " is " << num / i << std::endl;
				return 0;
			}
		}
		
		std::cout << "No solution was found!" << std::endl;


		return 0;
	}
	catch (std::exception e)
	{
		std::cerr << e.what() << std::endl;
	}
	catch (...)
	{
		std::cerr << "Unknown Error" << std::endl;
	}
}

bool isPrime(int num)
{
	for (auto i = 2U; i < num; ++i)
	{
		if (num % i == 0)
			return false;
	}

	return true;
}