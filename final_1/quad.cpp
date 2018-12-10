#include <iostream>
#include <cmath>


double discriminant(double a, double b, double c){
      double equation=(b*b)-(4*a*c);

      return equation;
}

double quadsolve(double a, double b, double c){
  double x = discriminant(a,b,c);
  double root = sqrt(x);
  double integer = (-b + root);
  double amount = integer/(2*a);

  if (x >=0){
    std::cout << "+Root:" << amount<<'\n';
  }
  else
  }
    std::cout << "-Root:" << 0 <<'\n';
  {
    return 0;
  }

int main()
{

  std::cout <<"The discriminant of a=3 b=4 c=5 is: " << discriminant(3,4,5) << '\n';
  std::cout << "The discriminant of a=2 b=6 c= 3 is: " << discriminant(2,6,3) << '\n';
  std::cout << quadsolve(2,6,3) << '\n';
  return 0;
}
