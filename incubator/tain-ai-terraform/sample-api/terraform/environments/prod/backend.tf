terraform {
  backend "s3" {
    region = "ap-northeast-2"
    bucket = "film-tfstate"
    key    = "prod/api-server.tfstate"
  }
}
