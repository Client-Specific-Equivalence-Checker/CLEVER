int lib(int x) {
  return x | 1;
}

int client(int x){
  if (x % 2 == 0) {
    return lib(x);
  } else {
    return x;
  }
  return lib(x);
}

int main() {
	int x;
	return client(x);
}
