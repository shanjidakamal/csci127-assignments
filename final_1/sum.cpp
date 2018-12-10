#include <iostream>
#include <cmath>

int sumOfSquares(int a, int b){
  int amount;
  int value=0;
  if (a<b)
  {
    for (size_t i = a; i <= b; i++) {
      int square= pow(i,2);
      value= value + square;
    }
  }
  else
  {
    std::cout << "not possible because a>b/" << '\n';
  }
    std::cout << value << '\n';
    return 0;
  }

int main()
{
  std::cout << sumOfSquares(5,10) << '\n';
  return 0;
}
