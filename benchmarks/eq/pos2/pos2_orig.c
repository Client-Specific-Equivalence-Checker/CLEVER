
int lib(int x) {
	int counter = 0;
	while (x < 0) {
		x++;
		counter++;
	}
	return counter;
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
