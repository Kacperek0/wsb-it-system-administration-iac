terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.36.0"
    }
  }
  backend "azurerm" {
    resource_group_name  = "wsb-demo-tf-backend"
    storage_account_name = "wsbtfbackend1812"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}
