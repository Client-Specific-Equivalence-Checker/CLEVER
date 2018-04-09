int lib(int x) {
	if (x < 5)
		return 5;
	else
		return x;
}

int client(int x){
	if (x < -100 || x > 100) {
		return x;
	}
	if (x < 0){
		return -lib((-x)*5)/5;
	}else{
		return lib((x+1)*5)/5 - 1;
	}
}

int main() {
	int x;
	return client(x);
}
