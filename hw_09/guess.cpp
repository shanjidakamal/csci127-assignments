//Ask the user to input an integer between 0 and 99 inclusive
//(using ~std::cin).
//The compute will use a while loop. In the loop it will guess
//the user's answer and then adjust up or down until it guesses
//correctly.
//user if the number is higher, lower, or correct. The user will
//lower than the guess, 1 to represent that the number is higher
//than the guess and 0 if the number i the guess.

#include <iostream>

#include <cstdlib>
#include<ctime>

int main()
{
//  int i;
//  int i2= 1+rand() % 100;
//  do {
//    std::cout << "Please enter a number(0-100):" << '\n';
//    std::cin >> i ;
//    if (i<i2)
//    {
//      std::cout << "Number Low, Try Again" << '\n';
//    }
//    else if(i>i2)
  //  {
  //    std::cout << "Number High, Try Again" << '\n';
  //  }
  //  else if(i == i2)
  //  {
    //  std::cout << "Correct number" << '\n';
    //}
//  } while(i!=i2);

  //std::cout << "Please enter a number:" << '\n';
  //std::cin >> i ;
  srand(time(NULL));
  int answer = rand ()%100;

  int guess;

  std::cout << answer << '\n';
  std::cout << "Please enter a guess: " << '\n';
  std::cin >> guess;
  int guesses=1;
  while (guess!=answer) {
    if (guess>answer) {
      std::cout << "You guessed to high" << '\n';
    } else if (guess<answer) {
      std::cout << "You guessed to low" << '\n';
    }

    std::cout << "Please enter a guess: " << '\n';
    std::cin >> guess;
    guesses ++;
  }
  std::cout << "Congratulations You Guessed Right!" << '\n';
  std::cout << "It took you " << guesses<<" guesses.\n";
  //std::cout << answer<<"\n";
  //answer=rand()%100;
  //std::cout << "answer" << '\n';
  return 0;

}
