class Logger {
  final String name;

  static final Map<String, Logger> _cache = <String, Logger>{};
//Factory constructors have no access to this. That’s why we have declared _cache as static.
  factory Logger(String name) {
    return _cache.putIfAbsent(name, () => Logger._internal(name));
  }
  // private constructor
  Logger._internal(this.name) {
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
