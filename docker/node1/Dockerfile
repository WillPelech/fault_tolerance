FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN set -eux; \
  rm -rf /var/lib/apt/lists/*; \
  apt-get update; \
  apt-get install -y --no-install-recommends ca-certificates; \
  rm -rf /var/lib/apt/lists/*

# Now HTTPS is safe
RUN sed -i 's|http://ports.ubuntu.com/ubuntu-ports|https://ports.ubuntu.com/ubuntu-ports|g' /etc/apt/sources.list

RUN set -eux; \
  rm -rf /var/lib/apt/lists/*; \
  apt-get update -o Acquire::Retries=5 -o Acquire::http::Pipeline-Depth=0; \
  apt-get install -y --no-install-recommends \
    bash curl iputils-ping netcat-openbsd build-essential; \
  rm -rf /var/lib/apt/lists/*

CMD ["bash"]
