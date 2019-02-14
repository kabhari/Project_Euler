/*

Problem Statement:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

src: https://projecteuler.net/problem=1

*/

#include <stdio.h>
#include <iostream>

// function decalration
int SumFunc(int number, int div);

int main(int argc, char** argv)
{

	try 
	{
		// default max is 1000 but allow user can override
		auto max = (argc > 1) ? atoi(argv[1]) : 1000;

		// init
		auto sum(0);

		// Solution 1 ( O(n) )
		for (auto i = 1U; i < max; ++i)
		{
			if (i % 3 == 0 || i % 5 == 0)
				sum += i;
		}

		// print result
		std::cout << "Solution 1 Sum is: " << sum << std::endl;

		// Solution 2 ( O(1) )
		sum = SumFunc(max - 1, 3) + SumFunc(max - 1, 5) - SumFunc(max - 1, 15); // have to deduct 15 since it's counted twice

		// print result
		std::cout << "Solution 2 Sum is: " << sum << std::endl;
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

int SumFunc(int max, int div)
{
	// sum of numbers less than max & divisible by div is: div * ( 1 + 2 + ... + max / div) [formula 1]
	// using the summation formula: https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF [formula 2]
	// let's rewrite fromula 1 using formula 2: div * ( max / div ) * ( ( max / div ) + 1 ) / 2

	return div * (max / div) * ((max / div) + 1) / 2;
}