
int lib(int x) {
	if (x < 0){
		return -x;
	}else{
    while (x >= 0) {
      x = x;
    }
		return x;
	}
}

int client(int x){
	if (x > 0) {
		return -lib(-x);
	}else{
		return lib(x);
	}
}

int main() {
	int x;
	return client(x);
}
