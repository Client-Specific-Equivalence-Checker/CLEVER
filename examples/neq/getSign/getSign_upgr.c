int lib(int x) {
  if (x <= 0)
     return -1;
  else
     return 1;
}

int client(int x){
  return lib(x);
}

int main() {
	int x;
	return client(x);
}
