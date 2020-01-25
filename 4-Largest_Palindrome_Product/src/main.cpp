/*

Problem Statement: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

src: https://projecteuler.net/problem=4

*/


#include <stdio.h>
#include <iostream>

bool isPalindromic(int num);

int main(int argc, char** argv)
{
	try
	{
		
		int largestPalindrome(0);

		for (auto i = 999U; i > 99; --i)
		{
			for (auto j = i; j > 99; --j)
			{
				if (isPalindromic(i*j) && largestPalindrome < i*j)
				{
					largestPalindrome = i * j;
				}
			}
		}

		if (largestPalindrome > 0)
		{
			std::cout << "The largest palindrome made from the product of two 3-digit numbers is " << largestPalindrome << std::endl;
			return 0;
		}

		std::cout << "Could not find a solution!" << std::endl;
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

bool isPalindromic(int num)
{
	// we need to construct the reversed number and see if it matches with original one
	int reversed(0), remainder(0), original(num);

	while (num > 0)
	{
		remainder = num % 10;
		reversed = reversed * 10 + remainder;
		num /= 10;
	}

	return (reversed == original ? true : false);
}