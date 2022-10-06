class Logger {
  final String name;
  Logger(this.name) {
    print("New logger created with name $name");
  }
  void log(String msg) {
    print("$name : $msg");
  }
}

class A {
  late final Logger _logger;
  A() {
    _logger = Logger('A');
  }
}

void t1() {
  for (int i = 1; i <= 5; i++) {
    print("Creating instance ${i}");
    A a = A();
    print(""); //newline
  }
}

void t2() {}
