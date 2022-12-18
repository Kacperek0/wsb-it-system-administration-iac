resource "azurerm_storage_account" "storage_account" {
  name                     = "${var.name}9g74ht9g8u3"
  resource_group_name      = var.resource_group
  location                 = "West Europe"
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = var.tags
}

