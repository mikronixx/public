#images
# download latest ghost image
resource "docker_image" "image_id" {
  name = "${var.image}"
}

