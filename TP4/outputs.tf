output "resource_group_name" {
  value = var.azure_resource_group_name
}

output "public_ip_address" {
  value = azurerm_linux_virtual_machine.main_virtual_machine.public_ip_address
}

output "private_key" {
  value     = tls_private_key.main_ssh_key.private_key_pem
  sensitive = true
}

resource "local_file" "private_key" {
  content         = tls_private_key.main_ssh_key.private_key_pem
  filename        = "${path.module}/id_rsa"
  file_permission = "0600"
}