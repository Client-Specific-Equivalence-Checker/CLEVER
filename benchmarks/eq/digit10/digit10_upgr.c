int f(int n) {
    int result = 1;
    int b = 1;
  	int counter =1;
    int retval = -1;

    while (!(b == 0)) {
        if (n < counter * 10) {
            retval = result;
            b = 0;
        } else if (n < counter *100) {
            retval = result + 1;
            b = 0;
        } else if (n < counter * 1000) {
            retval = result + 2;
            b = 0;
        } else if (n < counter * 10000) {
            retval = result + 3;
            b = 0;
        } else {
            counter = counter * 10000;
            result = result + 4;
        }
    }
    return retval;
}
