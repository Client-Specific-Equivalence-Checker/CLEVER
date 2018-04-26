int lib(int n) {
  int a =0;
  int b =1;
  int i =0;

  while ( i < n){
    i = i +1;
    int a_old = a;
    int b_old = b;
    a = b_old;
    b = a_old + b_old;
  }
  return a;
}

int client(int x){
  if (x <5 ) {
    return lib(x);
  }
  return 0;
}

int main() {
	int x;
	return client(x);
}


