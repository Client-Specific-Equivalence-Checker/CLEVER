int lib(int x, int y) {
  if (x < y) {
    int temp = x;
    x = y;
    y = temp;
  }
  return (x - y);
}

int client(int c, int d){
  if (c > d ) {
    return lib(c, d);
  } else {
    return lib(d, c);
  }
}

int main() {
	int a;
  int b;
	return client(a , b);
}
