int lib(int x, int y) {
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
