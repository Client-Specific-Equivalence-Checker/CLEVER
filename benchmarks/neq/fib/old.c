int lib(int n) {
  if (n ==1){
    return 1;
  }else{
    lib(n - 1) + lib(n - 2);
  }
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


