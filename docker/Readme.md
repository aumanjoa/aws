Configure Docker to start on root

```bash
sudo systemctl enable docker
```

Run the docker container

```bash
docker run --name aws-hello-container -d -p 80:80 --restart unless-stopped aumanjoa/aws-hello
```

