# Linode provider block. Installs Linode plugin.
terraform {
  required_providers {
    linode = {
      source = 'linode/linode'
      version = '1.16.0'
    }
  }
}
provider "linode" {
  token = "${var.token}"
}

variable "region" {
  description = "This is the location where the Linode isntance is peloyed"
}

/* A multi
   line comment. */
resource "linode_instance" "example_linode" {
  image = "linode/ubuntu18.04"
  label = "example-linode"
  region = "${var.region}"
  type = "g6-standart-1"
  authorized_keys = [ "my-key" ]
  root_pass = "example-password"
}

#===== пример от Merion Academy ===============
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}