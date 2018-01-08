
int lib(int x) {
	if (x < 0){
		return -x;
	}
	int counter = 0;
	while (x > 0) {
	    x += 1;
		counter += 1;
	}
	return counter;
}

int client(int x){
	if (x < 0) {
		return lib(x);
	}
	return -x;
}

int main() {
	int x;
	return client(x);
}
