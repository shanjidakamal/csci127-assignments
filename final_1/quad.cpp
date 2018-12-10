#include <iostream>
#include <math.h>
#include <string>


double discriminant(double a, double b, double c){
      double equation=(b*b)-(4*a*c);

      return equation;
}

double quadsolve(doubleAmount){
  if doubleAmount >= 0;
      return sqrt(doubleAmount);
  else;
    return "NOT POSSIBLE";

}



int main()
{

  std::cout <<"The discriminant of a=3 b=4 c=5 is: " << discriminant(3,4,5) << '\n';
  std::cout << "The discriminant of a=2 b=6 c= 3 is: " << discriminant(2,6,3) << '\n';
  std::cout << quadsolve(discriminant(2,6,3)) << '\n';
  return 0;
}
