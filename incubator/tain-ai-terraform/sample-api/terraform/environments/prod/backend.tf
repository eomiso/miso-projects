terraform {
  backend "s3" {
    region = "ap-northeast-2"
    bucket = "aesop-film-tfstate"
    key    = "prod/api-server.tfstate"
  }
}
