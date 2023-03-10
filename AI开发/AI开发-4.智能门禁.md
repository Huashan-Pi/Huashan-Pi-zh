[toc] 

---
<div STYLE="page-break-after: always;"></div>

> note：使用前请确保配置好相关环境，未配置见《软件安装编译环境搭建》

> 需要sensor_cfg.ini文件！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！（已完成！）
>
> 需要后台操作！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！

# 门禁APP，人脸识别

## 1、如何编译门禁APP
    # 初始化编译环境
    1.cd cvi_media_sdksdk/
    2.source build/cvisetup.sh 
    3.defconfig cv1812h_wevb_0007a_emmc
    4.build_all
    
    # 编译门禁应用app，生成相关文件
    5.cd ../product-sample/access-guard-turnkey/
    6.cp customer/cvitek/cv1821h_musl_lvgl_aisdk_emmc_appconfig .config   # 编译配置文件
    7.make clean&&make &&make install
    
    # 可以在以下目录中看到install文件夹和app_install.tar
    
    chile@chile-VirtualBox:~/temp/sophpi-huashan/product-sample/access-guard-turnkey/customer/cvitek$ ls
    app_install.tar                             cv1835_awtk_appconfig        cvitek_vpss_config_aisdk.c  Others
    cv1821h_musl_lvgl_aisdk_emmc_appconfig      cv1835_lvgl_aisdk_appconfig  cvitek_vpss_config_aisdk.o
    cv182x_lvgl_aisdk_spinand_appconfig         cvitek_gui_ext.c             cvitek_vpss_config.c
    cv182x_uclibc_lvgl_aisdk_spinand_appconfig  cvitek_gui_ext.o             install

> .config文件内容，根据需要配置

```
CONFIG_CUSTOMER="cvitek"
# CONFIG_CVI_SOC_CV183X is not set
# CONFIG_CVI_SOC_CV182X is not set
CONFIG_CVI_SOC_CR182X=y
# CONFIG_APP_32BIT is not set
# CONFIG_APP_64BIT is not set
# CONFIG_APP_UCLIBC is not set
CONFIG_APP_MUSL=y
CONFIG_MW_SDK_VER_MUSL=y
CONFIG_ENABLE_GUI_LVGL=y							#LVGL GUI界面使能
# CONFIG_ENABLE_GUI_AWTK is not set
CONFIG_ALGORITHM_VENDOR_AISDK=y
# CONFIG_ALGORITHM_VENDOR_MEGVII is not set
# CONFIG_ALGORITHM_VENDOR_SENSETIME is not set
CONFIG_ALGORITHM_VENDOR="aisdk"

#
# Main app config
#应用功能配置
#
CONFIG_DUAL_SENSOR_SUPPORT=y					#摄像头相关配置
CONFIG_SENSOR0_IS_RGB=y
CONFIG_ENABLE_ISPD=y
CONFIG_INPUT_TP=y
# CONFIG_INPUT_KB is not set
# CONFIG_BUILD_APP is not set
CONFIG_BUILD_APP_LEGACY=y
# CONFIG_VI_ROTATION_NONE is not set
CONFIG_VI_ROTATION_90=y
# CONFIG_VI_ROTATION_180 is not set
# CONFIG_VI_ROTATION_270 is not set
CONFIG_VO_ROTATION_NONE=y						#视频输出不旋转
# CONFIG_VO_ROTATION_90 is not set
# CONFIG_VO_ROTATION_180 is not set
# CONFIG_VO_ROTATION_270 is not set
# CONFIG_VPSS_VIDEO_FLIP_SUPPORT is not set
# CONFIG_VPSS_VIDEO_MIRROR_SUPPORT is not set
CONFIG_RGB_VIDEO_RTSP_SUPPORT=y
# CONFIG_RGB_VIDEO_RTSP_VENC_BIND_VI is not set
CONFIG_RGB_VIDEO_RTSP_VENC_BIND_VPSS=y
# CONFIG_RGB_VIDEO_RTSP_VENC_BIND_DISABLE is not set
CONFIG_IR_VIDEO_RTSP_SUPPORT=y
# CONFIG_IR_VIDEO_RTSP_VENC_BIND_VI is not set
CONFIG_IR_VIDEO_RTSP_VENC_BIND_VPSS=y
# CONFIG_IR_VIDEO_RTSP_VENC_BIND_DISABLE is not set
# CONFIG_ISP_FACE_AE_SUPPORT is not set
# CONFIG_WEBSERVER_SUPPORT is not set
# CONFIG_FILE_STORAGE_SUPPORT is not set
# CONFIG_FILE_PLAYER_SUPPORT is not set
# CONFIG_ETHERNET_SUPPORT is not set
# CONFIG_WIFI_SUPPORT is not set
# CONFIG_BLUETOOTH_SUPPORT is not set
# CONFIG_AUDIO_PLAYER_SUPPORT is not set
CONFIG_FACTORY_TEST_SUPPORT=y
# end of Main app config

#
# Customer app config
#
CONFIG_USE_DEFAULT_PQ_PARAM=y
CONFIG_PANEL_DISPLAY_SUPPORT=y
CONFIG_PANEL_DISPLAY_HOR=720					#显示分辨率设置
CONFIG_PANEL_DISPLAY_VER=1280
# end of Customer app config

#
# Function libs config
#
# CONFIG_ADVERTISEMENT_SUPPORT is not set
CONFIG_AUDIO_SUPPORT=y							#声音支持
CONFIG_BOOTLOGO_SUPPORT=y
# CONFIG_FINGERPRINT_SUPPORT is not set
# CONFIG_QRCODE_SUPPORT is not set
CONFIG_DATABASE=y								
CONFIG_NFC_SUPPORT=y							#NFC支持
# end of Function libs config

# CONFIG_DEBUG_VER is not set
# CONFIG_STATIC_LINK is not set
```





> 输出结果如下

```shell
......

install/res/mipmap-mdpi_bk/sy-tkqx.png
install/res/mipmap-mdpi_bk/24.png
install/res/mipmap-mdpi_bk/18.png
install/res/mipmap-mdpi_bk/sy-zs4.png
install/res/mipmap-mdpi_bk/1.png
install/res/mipmap-mdpi_bk/union-117.png
install/res/mipmap-mdpi_bk/10.png
install/res/mipmap-mdpi_bk/7.png
install/res/mipmap-mdpi_bk/sy-yl.png
install/res/mipmap-mdpi_bk/sz-wlxz.png
install/res/mipmap-mdpi_bk/sy-zs7.png
install/res/mipmap-mdpi_bk/tk-bj.png
install/res/mipmap-mdpi_bk/sy-dj1-h.png
install/res/mipmap-mdpi_bk/rlk-ss.png
install/res/mipmap-mdpi_bk/20.png
install/res/mipmap-mdpi_bk/wlsz-wifi.png
install/res/mipmap-mdpi_bk/hmd-bk.png
install/res/mipmap-mdpi_bk/sz-gxh.png
install/res/mipmap-mdpi_bk/db-fh.png
install/res/mipmap-mdpi_bk/12.png
install/res/mipmap-mdpi_bk/25.png
install/res/mipmap-mdpi_bk/sy-zs3.png
install/res/mipmap-mdpi_bk/sy-lj1.png
install/res/mipmap-mdpi_bk/sbcg-zs.png
install/res/mipmap-mdpi_bk/gray_scale.png
install/res/mipmap-mdpi_bk/5.png
install/res/mipmap-mdpi_bk/sy-tkqr.png
install/sample_dsi
install/sensor_cfg_gc2093.ini
install/sensor_cfg_imx307.ini
install/auto.sh
install/sensor_cfg.ini
install/cvimodel/
install/cvimodel/fqnet-v5_shufflenetv2-softmax.cvimodel
install/cvimodel/cviface-v5-s.cvimodel
install/cvimodel/liveness-rgb-ir.cvimodel
install/cvimodel/retinaface_mnet0.25_608_342.cvimodel
install/uninstall.sh
install/sac_application.bin
chile@chile-VirtualBox:~/sophpi-huashan/product-sample/access-guard-turnkey$

```

<div STYLE="page-break-after: always;"></div>

## 2、配置板端资源以及环境

```shell
1.把app_install.tar压缩包拷贝到板端/mnt/data后解压：
  cd /mnt/data/
  tar -xvf app_install.tar
  解压后的文件会放在install文件夹中
  还需要把sophpi-huashan/cvi_media_sdksdk/middleware/v2/sample/mipi_tx/下的sample_dsi放到install文件里：
  cp ../sd/sample_dsi install/
  将摄像头参数配置文件放到/mnt/data目录下，源文件为sophpi-huashan/cvi_media_sdk/middleware/v2/sample/sensor_cfg/sensor_cfg.ini.gc2053+gc2093：
  cp sensor_cfg.ini.gc2053+gc2093 /mnt/data/sensor_cfg.ini
2.配置环境变量:		
    export INSTALL_PATH=/mnt/data/install
    export LD_LIBRARY_PATH="/lib:/lib/arm-linux-gnueabihf:/usr/lib:/usr/local/lib:/mnt/system/lib:/mnt/system/usr/lib:/mnt/system/usr/lib/3rd:$INSTALL_PATH/lib"
    export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/mnt/system/usr/bin:/mnt/system/usr/sbin:/mnt/data/bin:/mnt/data/sbin"
    export HASPUSER_PREFIX=/mnt/data/auth
    
    # 设置isp参数文件，程序默认从该路径加载
    mv /mnt/cfg/tmp_secure  /mnt/cfg/param
3.运行sample_dsi 或 启动屏幕驱动：
    cd /mnt/data/install	
    ./sample_dsi # 使用LCD接口
    devmem 0x0a088000 32 0xC0
4.加载fb对应的ko:
    insmod /mnt/system/ko/cfbcopyarea.ko 
    insmod /mnt/system/ko/cfbfillrect.ko 
    insmod /mnt/system/ko/cfbimgblt.ko 
    insmod /mnt/system/ko/cvi_fb.ko
    insmod /mnt/system/ko/3rd/gt9xx.ko
5.运行gui程序：
    ./sac_application.bin &
```



## 3、功能介绍及运行效果

### 3.1 功能介绍

对人脸进行检测并保存脸部特征，识别到设定的人脸后输出信息提示

### 3.2 运行效果

> 终端输出如下

```
...

light val = 355
idx:0  liveness score:0.029362
light val = 351
idx:0  liveness score:0.047770
light val = 348
idx:0  liveness score:0.034316
light val = 347
idx:0  liveness score:0.052124
light val = 347
idx:0  liveness score:0.029247
light val = 348
idx:0  liveness score:0.055709
light val = 348
idx:0  liveness score:0.033816
light val = 364
idx:0  liveness score:0.014258
light val = 357
light val = 352
light val = 351
light val = 349
light val = 344
light val = 340
light val = 337
light val = 335
light val = 346
light val = 347
light val = 351
idx:0  liveness score:0.020436				

...
```

> 屏幕显示如下

<img src="../assert/AI开发-4.智能门禁/image-20221212152514365.png" alt="image-20221212152514365" style="zoom:20%;" />





