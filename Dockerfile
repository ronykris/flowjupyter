FROM python:3-alpine

RUN apk --update add nano
RUN python -m pip install --upgrade pip
RUN apk add gcc musl-dev linux-headers python3-dev
RUN pip3 install notebook bash_kernel
RUN python3 -m bash_kernel.install

RUN mkdir -p /root/.local/share/jupyter/kernels/flowjupyter
RUN mkdir -p /root/flowjupyter

COPY kernel.json /root/.local/share/jupyter/kernels/flowjupyter/

EXPOSE 8888

CMD ["jupyter", "notebook", "--allow-root --ip 0.0.0.0 --no-browser"]