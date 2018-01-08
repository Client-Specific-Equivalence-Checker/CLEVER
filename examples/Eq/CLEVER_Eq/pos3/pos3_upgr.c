int lib(int x) {
	if (x < 0){
		return -x;
	}
	return x;
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
