int lib(int n) {
  if (n <= 0){
     return 0;
     }else if(n == 1){
        return 1;
     }else{
        return n * lib(n);
     }
}

int client(int x){
  if (x < 5) {
    return lib(x);
  }
  return 0;
}

int main() {
	int x;
	return client(x);
}

