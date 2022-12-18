resource "azurerm_resource_group" "resource_group" {
  name     = "wsb-${var.name}-rg"
  location = "West Europe"

  tags = var.tags
}
