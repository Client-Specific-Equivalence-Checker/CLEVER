
int lib(int x) {
	if (x < 0){
		return -x;
	}else{
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
	int x;//=3089104896;
	return client(x);
}
