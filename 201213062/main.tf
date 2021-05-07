provider "google"{
    credentials = file("practica-312603-3aae22ea52d7.json")
    project = "practica-312603"
    region = "us-west1"
}

resource "random_id" "instance_id"{
    byte_length = 8
}

// crear mi maquina virtual

resource "google_compute_instance" "default" {
    name = "practica-312603--${random_id.instance_id.hex}"  
    machine_type = "f1-micro"
    zone = "us-west1-a"

    boot_disk {
      initialize_params {
          image = "debian-cloud/debian-9"
      }
    }

    metadata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python-pip rsync; pip install flask"

    network_interface {
      network = "default"

      access_config {
        
        //leer la ip publica

      }
    }

    metadata = {
      ssh-keys = "monica-261:${file("~/.ssh/id_rsa.pub")}"
    }
}

output "ip" {
    value = google_compute_instance.default.network_interface.0.access_config.0.nat_ip
}