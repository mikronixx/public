container_name = {
  dev = "dev_blog"
  prod = "prod_blog"
}

image = {
  #dev = "ghost:latest"
  dev = "ghost:alpine"
  prod = "ghost:alpine"
}

int_port = {
  dev = "2368"
  prod = "2368"
}

ext_port = {
  dev = "8888"
  prod = "80"
}

