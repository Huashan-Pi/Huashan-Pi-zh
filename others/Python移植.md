[toc]

# 开发板移植Python

> 以python3.8.0为例
在开发板上搭建python开发环境，实现python基础开发



## 1、工具及环境准备

### 1.1 软件
Ubuntu20.04、MobaXterm

### 1.2 硬件
华山派、SD卡、usb-tt

### 1.3 编译环境
ubuntu虚拟机预装python环境



## 2、交叉编译

### 2.1 配置交叉编译链

```
# 添加交叉编译工具链路径到环境变量
cd sophpi-huashan/mmf-sdk/
source build/cvisetup.sh
defconfig cv1812h_wevb_0007a_emmc

# 获取root权限 （后面可能会出现一下安装权限问题）
sudo -i
```

### 2.1 获取python源码

```sh
# 获取Python3.8.0源码
git --branch v3.8.0 https://github.com/python/cpython.git		# 文件夹名为cpython
```

### 2.3 设置编译参数及配置文件

```sh
cd cpython

# 配置生成makefile文件
./configure --host=riscv64-unknown-linux-musl  --disable-ipv6 --prefix=$PWD/_instal  ac_cv_file__dev_ptc=no  ac_cv_file__dev_ptmx=no  --build=x86_64-linux-gnu  --enable-shared

# 修改Makefile，添加编译选项
vi Makefile
```
> 文件修改内容，添加编译选项

```makefile
...

# === Variables set by configure
VERSION=        3.8
srcdir=         .

abs_srcdir=     /home/kevin/Python-3.8.0
abs_builddir=   /home/kevin/Python-3.8.0

RV64_FLAGS +=  -march=rv64imafdcvxthead -mcmodel=medany -mabi=lp64d

CC=             riscv64-unknown-linux-musl-gcc $(RV64_FLAGS)
CXX=            riscv64-unknown-linux-musl-c++ $(RV64_FLAGS)
MAINCC=         $(CC)
LINKCC=         $(PURIFY) $(MAINCC)
AR=             riscv64-unknown-linux-musl-ar
READELF=        riscv64-unknown-linux-musl-readelf $(RV64_FLAGS)
SOABI=          cpython-38-riscv64-linux-gnu
LDVERSION=      $(VERSION)$(ABIFLAGS)
LIBPYTHON=
GITVERSION=
GITTAG=
GITBRANCH=
PGO_PROF_GEN_FLAG=-fprofile-generate
PGO_PROF_USE_FLAG=-fprofile-use -fprofile-correction

...
```

### 2.4 编译安装

```
make && make install
```

> 编译完成，可以在 `_instal` 文件夹下看到以下

```
root@chile-VirtualBox:/home/chile/cpython/_instal# ls
bin  include  lib  share
```

将 `bin/` 和 `lib/` 打包成 `cpy.tar` ，方便传输
```
tar -cvf cpy.tar bin lib
```



## 3、移植到板端使用


> 以下均在板端操作

### 3.1 传输打包文件到开发板

将上面打包的 `cpy.tar` 文件放到sd卡（也可以用scp传输，前面介绍使用过）
然后把sd卡插入开发板卡槽

```
# 开发板挂载sd卡
mount /dev/mmcblk1p1 /mnt/sd

# 把 cpy.tar 复制过来
cd /mnt/data
cp ../sd/cpy.tar ./

# 解压
tar -xvf cpy.tar 
```

### 3.2 配置使用

```
cd cpy

# 添加python依赖库路径
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/data/cpy/lib

# 使用python打印helloworld
./bin/python3.8
```

> 输出打印

```
[root@cvitek]/mnt/data/cpy# python3.8
Python 3.8.0 (tags/v3.8.0:fa919fdf25, Oct 27 2022, 20:22:10)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello,world")
hello,world
>>>

```
