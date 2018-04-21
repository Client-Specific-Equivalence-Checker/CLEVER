int f(int n) {
  int result = 1;
  int counter =10;

  while ( n >= counter) {
    result++;
    counter = counter * 10;
    if ( n >= counter) {
      result++;
      counter = counter * 10;
      if ( n >= counter) {
        result++;
        counter = counter * 10;
        if ( n >= counter) {
          result++;
          counter = counter * 10;
        }
      }
    }
  }
  return result;
}
