# build liteboots 镜像
FROM python:3.6.8-slim
# 设置编码
ENV LANG C.UTF-8
# 设置工作目录
WORKDIR /app
# 配置阿里云 pip 加速
COPY files/pip.conf /root/.pip/pip.conf
# 安装 python 依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# copy 模型文件 t2t_data
COPY t2t_data/ /app/t2t_data/
# 配置 tensor2tensor
COPY files/data_generators/ /usr/local/lib/python3.6/site-packages/tensor2tensor/data_generators/
# copy 代码到工作目录上
COPY . .

EXPOSE 5000
ENV ENV=prod\
    T2T_DATA_DIR=/app/t2t_data
# 设置启动命令
CMD python my_tf.py
