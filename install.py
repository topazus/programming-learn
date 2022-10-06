import shlex
import subprocess
print('installing flutter')
version='3.3.2'
url=f'https://storage.flutter-io.cn/flutter_infra_release/releases/stable/linux/flutter_linux_{version}-stable.tar.xz'
subprocess.run(shlex.split(f'wget {url}'))


print('installing Go language')
version=subprocess.run('curl https://go.dev/VERSION?m=text'.split())
url=f'https://storage.flutter-io.cn/flutter_infra_release/releases/stable/linux/flutter_linux_{version}-stable.tar.xz'
subprocess.run(shlex.split(f'wget {url}'))
