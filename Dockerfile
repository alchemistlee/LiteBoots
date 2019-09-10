FROM wangweijie/oss-tools:version-1.1 as downloader
# 模型版本
ENV VERSION v13
# oss 下载参数
ENV ACCESS_KEY_ID LTAITFQMrCFZSSF3
ENV ACCESS_KEY_SECRET Y6VgcVuhgmG7kuutVpXdr1D82jc1sz
ENV BUCKET_NAME tigerobo-infra
ENV ENDPOINT oss-cn-shanghai-internal.aliyuncs.com
# 设置下载目录
WORKDIR /data
# 下载模型文件
RUN python /app/download.py -f translate/models/${VERSION}/t2t_data.tgz

# 解压模型文件
FROM busybox as busybox
COPY --from=downloader /data/ /data/
RUN cd /data &&\
    tar -zxvf t2t_data.tgz

# build liteboots 镜像
FROM python:3.6.8-slim
# 设置编码
ENV LANG C.UTF-8
# 设置工作目录
WORKDIR /app
# copy 模型文件 t2t_data
COPY --from=busybox /data/t2t_data /app/t2t_data
# 配置阿里云 pip 加速
COPY files/pip.conf /root/.pip/pip.conf
# 安装 python 依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# 配置 tensor2tensor
COPY files/data_generators/ /usr/local/lib/python3.6/site-packages/tensor2tensor/data_generators/
# copy 代码到工作目录上
COPY . .

EXPOSE 5000
ENV ENV=prod\
    T2T_DATA_DIR=/app/t2t_data
# 设置启动命令
CMD python my_tf.py
