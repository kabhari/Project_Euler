/*

Problem Statement:

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

src: https://projecteuler.net/problem=2

*/


#include <stdio.h>
#include <iostream>

// function decalration
int fibonacci(int term);

int main(int argc, char** argv)
{
	try
	{
		// default max is 4 million but allow user can override
		auto max = (argc > 1) ? atoi(argv[1]) : 4000000;

		// Solution 1 (O(n))
		int a(1), b(2), c(0), sum(2);
			
		do
		{
			c = a + b;
			
			if (c % 2 == 0)
				sum += c;
			
			a = b;
			b = c;

		} while (c < max);

		std::cout << "Sum of the even-valued terms: " << sum << std::endl;

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

int fibonacci(int term)
{
	if (term == 1 || term == 2)
		return term;

	return fibonacci(term - 1) + fibonacci(term - 2);
}