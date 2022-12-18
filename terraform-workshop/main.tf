module "resource_group_module" {
  source = "./modules/resource_group"

  name = var.name
  tags = var.tags

}

module "storage_account_module" {
  source = "./modules/storage_account"

  name           = var.name
  resource_group = module.resource_group_module.resource_group

  tags = var.tags

}

module "storage_account_module2" {
  source = "./modules/storage_account"

  name           = "sysops2"
  resource_group = module.resource_group_module.resource_group

  tags = var.tags

}
