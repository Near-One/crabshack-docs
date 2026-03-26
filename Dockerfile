FROM python:3.12-slim AS builder
WORKDIR /docs
COPY . .
RUN pip install --no-cache-dir sphinx sphinx-wagtail-theme sphinx-copybutton \
    && sphinx-build -b html . /out

FROM nginx:alpine
COPY --from=builder /out /usr/share/nginx/html
EXPOSE 8080
RUN sed -i 's/listen\s*80;/listen 8080;/' /etc/nginx/conf.d/default.conf
