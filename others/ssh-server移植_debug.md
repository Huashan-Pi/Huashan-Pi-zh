[toc]

# 开发板ssh-server移植




使用ssh实现远程登陆，解放串口，并且提供安全传输


## 1、工具及环境准备


### 1.1 软件

`ubuntu20.04`、`mobaxterm`

### 1.2 硬件

华山派、网线、sd卡、`usb-ttl`

## 2、源码文件部署

```sh
mkdir ssh_portable
cd ssh_portable

# 以下源码包均无版本要求
# 1.openssh-7.3p1源码下载
wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-7.3p1.tar.gz
tar -zxvf openssh-7.3p1.tar.gz

#2.openssl-1.0.1t源码下载
wget https://www.openssl.org/source/openssl-1.0.1t.tar.gz
tar -zxvf source/openssl-1.0.1t.tar.gz

#3.zlib-1.2.11源码下载
git clone --branch v1.2.11 https://github.com/madler/zlib.git
```

> 文件目录如下

```sh
root@chile-VirtualBox:/home/chile/ssh_portable# ls
openssh-7.3p1  openssl-1.0.1t  zlib
```

## 3、交叉编译源码


```
# 获取root权限
sudo -i			# 防止出现权限问题
```


### 3.1 zlib交叉编译

```
cd zlib

# 创建安装目录
mkdir /usr/local/openssl

#配置
./configure --prefix=/usr/local/zlib
```

> 修改makefile
```makefile
CC=riscv64-unknown-linux-musl-gcc
AR=riscv64-unknown-linux-musl-ar
RANLIB=riscv64-unknown-linux-musl-ranlib
CPP=riscv64-unknown-linux-musl-gcc -E
LDSHARED=riscv64-unknown-linux-musl-gcc
```

```
# 编译安装
make
make install
```


### 3.2 openssl交叉编译

```
cd openssl-1.0.1t/

# 创建安装目录
mkdir /usr/local/openssl

# 配置
./Configure --prefix=/usr/local/ssl os/compiler:riscv64-unknown-linux-musl-gcc -fPIC

# 编译安装
make
make install
```


### 3.3 openssh交叉编译

```
cd openssh-7.3p1/

# 创建安装目录
mkdir /usr/local/openssh

# 配置
./configure --host=arm-linux --prefix=/usr/local/openssh --with-zlib=/usr/local/zlib --with-ssl-dir=/usr/local/openssl --disable-etc-default-login --disable-strip CC=riscv64-unknown-linux-musl-gcc AR=riscv64-unknown-linux-musl-ar

# 编译安装
make		#不需要make install
```

### 3.4 

> j建议重新制作文件系统
>
> 方便文件修改

