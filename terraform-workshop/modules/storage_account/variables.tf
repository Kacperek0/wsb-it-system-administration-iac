variable "name" {
  type        = string
  description = "Resource group name"
}

variable "tags" {
  type        = map(any)
  description = "Predefined map of tags."
}

variable "resource_group" {
  type        = string
  description = "Associated resource group name."
}
